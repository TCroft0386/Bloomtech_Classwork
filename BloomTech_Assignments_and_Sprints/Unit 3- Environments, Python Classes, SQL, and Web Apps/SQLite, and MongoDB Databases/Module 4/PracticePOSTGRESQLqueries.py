from multiprocessing.reduction import duplicate
import sqlite3

# SQLITE QUERIES
# How many passengers survived, and how many died?
survived = 'SELECT COUNT(titanic.Survived) FROM titanic WHERE titanic.Survived=1'
dead = 'SELECT COUNT(titanic.Survived) FROM titanic WHERE titanic.Survived=0'
#How many passengers were in each class?
class1 = 'SELECT COUNT(titanic.Pclass) FROM titanic WHERE titanic.Pclass=1'
class2 = 'SELECT COUNT(titanic.Pclass) FROM titanic WHERE titanic.Pclass=2'
class3 = 'SELECT COUNT(titanic.Pclass) FROM titanic WHERE titanic.Pclass=3'
#How many passengers survived/died within each class?
class1_surv = 'SELECT COUNT(titanic.Pclass) FROM titanic WHERE titanic.Pclass=1 AND titanic.Survived=1'
class2_surv = 'SELECT COUNT(titanic.Pclass) FROM titanic WHERE titanic.Pclass=2 AND titanic.Survived=1'
class3_surv = 'SELECT COUNT(titanic.Pclass) FROM titanic WHERE titanic.Pclass=3 AND titanic.Survived=1'
#What was the average age of survivors vs nonsurvivors?
avg_age_surv = 'SELECT avg(titanic.Age) FROM titanic WHERE titanic.Survived=1'
avg_age_dead = 'SELECT avg(titanic.Age) FROM titanic WHERE titanic.Survived=0'
#What was the average age of each passenger class?
avg_age_per_class = 'SELECT avg(titanic.Age) FROM titanic GROUP BY titanic.Pclass'
#What was the average fare by passenger class? By survival?
avg_fare_per_class = 'SELECT avg(titanic.Fare) FROM titanic GROUP BY titanic.Pclass'
avg_fare_surv = 'SELECT avg(titanic.Fare) FROM titanic GROUP BY titanic.Survived'
#How many siblings/spouses aboard on average, by passenger class? By survival?
avg_siblings_class = 'SELECT avg(titanic."Siblings/Spouses Aboard") FROM titanic GROUP BY titanic.Pclass'
avg_sib_surv = 'SELECT avg(titanic."Siblings/Spouses Aboard") FROM titanic GROUP BY titanic.Survived'
#How many parents/children aboard on average, by passenger class? By survival?
avg_par_chil_class = 'SELECT avg(titanic."Parents/Children Aboard") FROM titanic GROUP BY titanic.Pclass'
avg_par_chil_surv = 'SELECT avg(titanic."Parents/Children Aboard") FROM titanic GROUP BY titanic.Survived'
#Do any passengers have the same name? 
duplicate_names = 'SELECT COUNT (DISTINCT titanic.Name) FROM titanic Group by name'


def connect_db(name='titanic.csv'):
    return sqlite3.connect(name)

def execute_query(conn,query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

conn = connect_db()
results = execute_query(conn, survived)

