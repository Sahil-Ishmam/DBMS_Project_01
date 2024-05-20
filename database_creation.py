import pymysql
import cryptography


# connect database 
db = pymysql.connect(
    host='localhost',
    user='root',
    password='@mysqlpassword202123',
    database="Spendium_DB"
)



# cursor to execute queries

cursor = db.cursor()




"""

# Execute query to create the database 
query = "CREATE DATABASE IF NOT EXISTS Spendium_DB"
cursor.execute(query)

 """