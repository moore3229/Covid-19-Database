import mysql.connector
from getpass import getpass
from mysql.connector import connect
from sqlalchemy import create_engine

connection = connect(host='localhost', user='root', password='****', database='covid')
cursor = connection.cursor()
#db_connection_str = 'mysql+pymysql://user:@localhost/covid' #'mysql+pymysql://username:password@hostaddress/databasename'
#engine = create_engine(db_connection_str)

#read and display
cursor.execute("SELECT * FROM states_info limit 5")
result = cursor.fetchall()
print(result)


#update data
cursor.execute("UPDATE states_info SET population = 5000000 where state = 'TX'")

#get state, population and avarage daily hospitalization by state in descending order of hospitalization rate
result = cursor.execute("SELECT state, population, avg_hospitalizedCurrently FROM  state_aggregations ORDER BY population/avg_hospitalizedCurrently DESC")
result = cursor.fetchall()
print(result)

