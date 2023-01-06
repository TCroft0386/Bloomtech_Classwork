import sqlite3

def create_sl_conn(name='rpg_db.sqlite3'):
    sl_conn = sqlite3.connect(name)
    return sl_conn

def execute_query(curs,query):
    result = curs.execute(query)
    return curs.fetchall()

get_characters = '''SELECT * From charactercreator_character;'''

sl_conn = create_sl_conn()
sl_curs = sl_conn.cursor()

characters = execute_query(sl_curs, get_characters)