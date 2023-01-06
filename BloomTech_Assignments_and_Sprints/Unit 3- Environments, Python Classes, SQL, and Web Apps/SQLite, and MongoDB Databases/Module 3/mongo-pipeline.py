import sqlite3
import pymongo

USER = 'LOlbrich'
PASSWORD = 'GNJwkTNFLjOv06lj'
SERVERNAME = 'Cluster0'

#open connection to mongo
def create_mdb_conn(PASSWORD, SERVERNAME, collection_name):
    client = pymongo.MongoClient(f"mongodb+srv://{USER}:{PASSWORD}@cluster0.u1dgs.mongodb.net/{SERVERNAME}?retryWrites=true&w=majority".format(USER,PASSWORD,SERVERNAME))
    # database that we want to connect to
    db = client[SERVERNAME]
    # create the collection so that we can insert into it
    collection = db[collection_name]
    return db

# this loop takes every rown of the dataframe we get from 
def char_doc_creation(mongo_db, character_list):
    for char in character_list:
        character_doc = {
            #since char will be a list we can index each value as such
            'name': char[1],
            'level': char[2],
            'exp': char[3],
            'hp': char[4],
            'strength': char[5],
            'intelligence': char[6],
            'dexterity': char[7],
            'wisdom': char[8],
            # add array of item names from newdict based on index from character_list
            # checks both dictionaries for values that are equal to the index 
            # and if it finds one, it adds it to the list which will immediatly 
            # be sent to the mongoDB through the insert_one statement 
            'items': newdict.get(char[0]),
            'weapons': weapdict.get(char[0])
        }
        mongo_db.characters.insert_one(character_doc)

# connection to sqlite3
def create_sl_conn(name='rpg_db.sqlite3'):
    sl_conn = sqlite3.connect(name)
    return sl_conn

# Execute query function
def execute_query(curs,query):
    curs.execute(query)
    return curs.fetchall()

get_characters = '''SELECT * FROM charactercreator_character, charactercreator_character_inventory GROUP BY charactercreator_character.character_id;'''
get_items = '''SELECT DISTINCT * FROM charactercreator_character_inventory WHERE charactercreator_character_inventory.item_id < 137'''
get_weapons = '''SELECT * FROM charactercreator_character_inventory WHERE charactercreator_character_inventory.item_id > 137'''
get_item_names = '''SELECT DISTINCT * FROM armory_item'''

if __name__ == '__main__':

    # creates database called 'characters' and creates a database object 
    db = create_mdb_conn(PASSWORD=PASSWORD,SERVERNAME=SERVERNAME,collection_name='characters')
    #print(db)

    #sqlite conn
    sl_conn = create_sl_conn()
    sl_curs = sl_conn.cursor()

    # geting char from sqlite 

    characters = execute_query(sl_curs, get_characters)
    # returns non-repeating list of character_id and names so we can iterate over
    # it in the main sending function to MongoDB

    list_of_items = execute_query(sl_curs, get_items)
    # returns item Id based on character id's inventory of item_id < 137

    get_item_names = execute_query(sl_curs, get_item_names)
    # returns item names with item_id

    list_of_weapons = execute_query(sl_curs, get_weapons)
    #returns item Id based on character id's inventory of item_id > 137

    #print(number_of_items[:10],'\n',list_of_items[:10],'\n',get_item_names[:10],'\n',list_of_weapons[:10])
    

    # want: list of item names per character ID and replace the item id with the name of the item
    newdict = {}
    for i in list_of_items:
        # i is every line of the result of the get_items query
        if i[1] not in newdict.keys():
            #if its not in the dictionary keys, make it one
            newdict[i[1]] = [i[2]]
        else:
            # if it is in the dictionary, add the second-index value of i to  
            # the key thats already there
            newdict[i[1]].append(i[2])

    # swaps index for name in dictionary, leaving character ID alone
    for i in newdict.values():
        # for every list in the dictionary
        for j in range(len(i)):
            #for every item in each list 
            i[j] = get_item_names[i[j]-1][1]
            #change the value at the current index based on the value of the 
            #thing at the current index and use that value AS the index 
            # for a list of all the item names which returns the exact location 
            # for the string name of the item. I.e. swaps the index for its own name


    # Exact same thing as other list but for weapons with item_id values over 137
    weapdict = {}
    for i in list_of_weapons:
        if i[1] not in weapdict.keys():
            weapdict[i[1]] = [i[2]]
        else:
            weapdict[i[1]].append(i[2])

    # swaps index for name in dictionary, leaving character ID alone
    for i in weapdict.values():
        for j in range(len(i)):
            i[j] = get_item_names[i[j]-1][1]
    
    #create documents in mongo, called last because we have to have the dicts loaded 
    # up with the data before we execute. Uses characters list as a index for 
    # iterating through sending the file to mongoDB
    char_doc_creation(db, characters)
