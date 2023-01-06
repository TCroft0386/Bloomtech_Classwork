import re
import pymongo

USER = 'LOlbrich'
PASSWORD = 'GNJwkTNFLjOv06lj'
SERVERNAME = 'Cluster0'

#open connection to mongo
def create_mdb_conn(collection_name):
    client = pymongo.MongoClient(f"mongodb+srv://{USER}:{PASSWORD}@cluster0.u1dgs.mongodb.net/{SERVERNAME}?retryWrites=true&w=majority")
    # database that we want to connect to
    db = client[SERVERNAME]
    # create the collection so that we can insert into it
    return db, client

#QUERIES
# TOTAL_CHARACTERS: How many total Characters are there?
total_char = {}
# 302

# TOTAL_ITEMS: How many total Items?
total_items = {}
# 174

# WEAPONS: How many of the Items are weapons? Not?
weapons = {'armory_weapon':{}}
    
# CHARACTER_ITEMS: How many Items does each character have? (Return first 20 rows)

char_item_count = {}


# CHARACTER_WEAPONS: How many Weapons does each character have? (Return first 20 rows)
char_weap_count = {}
char_weap_count = {'charactercreator_character_inventory':{}}

# AVG_CHARACTER_ITEMS: On average, how many Items does each Character have?
avg_items_count = {}
# 2.97
# AVG_CHARACTER_WEAPONS: On average, how many Weapons does each character have?
avg_char_weap = {}
db,cursor = create_mdb_conn('character')


tempdict = db.characters.find({})
for documents in tempdict:
    print(documents.values())
    