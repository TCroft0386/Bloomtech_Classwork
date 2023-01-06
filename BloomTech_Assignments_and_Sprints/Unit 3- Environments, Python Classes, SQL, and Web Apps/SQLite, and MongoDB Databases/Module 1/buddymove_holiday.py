import pandas as pd
import sqlite3
df = pd.read_csv('buddymove_holidayiq.csv')
conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
#df.to_sql('buddymove_holidayiq.csv',conn)

#QUERIES
count = 'SELECT COUNT(*) FROM buddymove_holidayiq'

num_above_100 =  '''SELECT COUNT(*) FROM buddymove_holidayiq
                    where Nature > 100 AND Shopping>100'''
                    
review_avg = '''SELECT avg(Nature),avg(Shopping),avg(Picnic),avg(Religious),
                avg(Sports),avg(Theatre) FROM buddymove_holidayiq'''                    

# DB CONNECTION
def connect_db(name='buddymove_holidayiq'):
    return sqlite3.connect(name)

# cursor execute query function
def execute_q(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    return cursor.fetchall()

results = execute_q(conn, review_avg)
print(results)




