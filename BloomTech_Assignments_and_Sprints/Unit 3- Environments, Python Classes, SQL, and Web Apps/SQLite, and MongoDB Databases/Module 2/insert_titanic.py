
import pandas as pd

# POSTGRESQL SERVER CONNECTION function: returns pg_conn and pg_curs
def connection():
    '''returns pg_conn, pg_curs in that order'''

    import psycopg2
    DBNAME = 'pzmmufbp'
    USER = 'pzmmufbp'
    PASSWORD = 'xgqS-FE8BW1iprF2FtlH1ckuCQH2iukF' 
    HOST = 'kashin.db.elephantsql.com'

    pg_conn = psycopg2.connect(dbname=DBNAME,
                                user=USER, 
                                password=PASSWORD,
                                host=HOST)
    pg_curs = pg_conn.cursor()
    return pg_conn, pg_curs

#call connection function using default values returns on left side of =
pg_conn, pg_curs = connection()

#this function allows us to modify a table we have already created with the 
#query table function
def modify_table(curs, conn, query):
    curs.execute(query)
    conn.commit()

#execute query function that creates cursor from connection
def execute_q(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    return cursor.fetchall()

################ONLY NEED TO CHANGE CONNECTION ABOVE############################

# TABLE FORMATTING FOR TITANIC DATA SET: gets executed as SQL commands
create_char_table = '''CREATE TABLE titanic 
                        ("ID" SERIAL NOT NULL PRIMARY KEY,
                        "Survived" INT NOT NULL,
                        "Pclass" INT NOT NULL,
                        "Name" VARCHAR(100) NOT NULL,
                        "Sex" VARCHAR(10) NOT NULL,
                        "Age" INT NOT NULL,
                        "Siblings/Spouses Aboard" INT NOT NULL,
                        "Parents/Children Aboard" INT NOT NULL,
                        "Fare" INT NOT NULL
                        );'''

# LOAD CSV as df                       
df = pd.read_csv('titanic.csv')
# query the table and if it already exists drop it
modify_table(pg_curs,pg_conn, "DROP TABLE IF EXISTS titanic")
# since none should exist now, make a new table
modify_table(pg_curs,pg_conn, create_char_table)

# Table creation from CSV File. For every value in df,modify the table with this
# schema and using an fstring to call the index of each row of the data frame.        
for character in df.values:
    modify_table(pg_curs,pg_conn, f'''INSERT INTO titanic ("Survived","Pclass", "Name",
                        "Sex","Age","Siblings/Spouses Aboard",
                        "Parents/Children Aboard","Fare")
                        VALUES ({character[0]},{character[1]},'{character[2]}','{character[3]}',{character[4]},{character[5]},{character[6]},{character[7]})''')

# give me the query result from execute query function, pass in just pg_conneection and query
def results(pg_conn, query):
    result = execute_q(pg_conn, query)
    return result

# QUERIES 
# COUNT OF DB -- 817
count = 'SELECT COUNT(*) FROM titanic'
print(results(pg_conn, count)) # calling the results function with my connection
#to the data base and my sql query. The sql query and connection get passed into
#execute_q which is the query execution function. That function then creates a 
#cursor from the connection and uses it to execute the query. Then once its executed
#the SQL command it returns the result with cursor.fetchall() now you have the 
#result of your executed command and it passes everything back up to the print 
#statement

# NUMBER OF survived -- 342
survived = '''SELECT COUNT("Survived") FROM titanic WHERE "Survived"=1;'''
print(results(pg_conn, survived))

# NUMBER OF dead -- 545
dead = '''SELECT COUNT("Survived") FROM titanic WHERE "Survived"!=1;'''
print(results(pg_conn, dead))

# NUMBER OF dead from class 3 -- 368
dead3 = '''SELECT COUNT("Survived") FROM titanic WHERE "Survived"!=1 AND "Pclass"=3;'''
print(results(pg_conn, dead3))

# NUMBER OF survived from class 1 -- 136
survived1 = '''SELECT COUNT("Survived") FROM titanic WHERE "Survived"=1 AND "Pclass"=1;'''
print(results(pg_conn, survived1))