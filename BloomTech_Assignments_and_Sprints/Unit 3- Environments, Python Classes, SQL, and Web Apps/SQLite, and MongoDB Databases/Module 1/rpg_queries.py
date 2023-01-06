import sqlite3

#QUERIES
# TOTAL_CHARACTERS: How many total Characters are there?
total_char = 'SELECT COUNT(*) FROM Charactercreator_characters'
# 302

# TOTAL_SUBCLASS: How many of each specific subclass (the necromancer table)?
total_subclass = 'SELECT COUNT(DISTINCT(mage_ptr_id)) FROM charactercreator_necromancer'
# 11

# TOTAL_ITEMS: How many total Items?
total_items = "SELECT COUNT(*) FROM armory_item"
# 174

# WEAPONS: How many of the Items are weapons?
weapons = 'SELECT COUNT(*) FROM armory_weapon'
# 37

# NON_WEAPONS: How many of the items are not weapons?
non_weapons ='''SELECT COUNT(armory_item.item_id), armory_weapon.item_ptr_id
                FROM armory_item, armory_weapon
                WHERE armory_item.item_id != armory_weapon.item_ptr_id'''
# 138

# CHARACTER_ITEMS: How many Items does each character have? (Return first 20 rows)
char_item_count ='''SELECT character_id,COUNT(item_id)
                    FROM  charactercreator_character_inventory
                    GROUP BY character_id
                    LIMIT 20'''


# CHARACTER_WEAPONS: How many Weapons does each character have? (Return first 20 rows)
char_weap_count ='''SELECT character_id,COUNT(item_id), armory_weapon.item_ptr_id
                    FROM  charactercreator_character_inventory, armory_weapon
                    WHERE item_id=armory_weapon.item_ptr_id
                    GROUP BY character_id
                    LIMIT 20'''


# AVG_CHARACTER_ITEMS: On average, how many Items does each Character have?
avg_items_count ='''SELECT avg(item_id) FROM (SELECT character_id, COUNT(item_id) as item_id
                    FROM  charactercreator_character_inventory
                    GROUP BY character_id)'''
# 2.97

# AVG_CHARACTER_WEAPONS: On average, how many Weapons does each character have?
avg_char_weap =  '''SELECT AVG("COUNT(aw.power)") FROM (
                    SELECT cc_char.name, cc_char.character_id, COUNT(aw.power)  FROM charactercreator_character AS cc_char
                    JOIN charactercreator_character_inventory AS cc_inv
                    ON cc_char.character_id = cc_inv.character_id
                    JOIN armory_item as ai
                    ON ai.item_id = cc_inv.item_id
                    LEFT JOIN armory_weapon as aw
                    ON aw.item_ptr_id = ai.item_id
                    GROUP BY cc_char.character_id)
                    '''
# 1.411



# DB CONNECTION
def connect_db(name='rpg_db.sqlite3'):
    return sqlite3.connect(name)

# cursor execute query function
def execute_q(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    return cursor.fetchall()

conn = connect_db()
results = execute_q(conn, avg_char_weap)
print(results)