import pymysql
import cryptography

# database connection
db = pymysql.connect(
    host="localhost",
    user='root',
    password = "@mysqlpassword202123",
    database="Spendium_DB"
)



# function to create table 
def create_table(table_name,cursor):
    query = f"""
            Create table if not exists{table_name}(
            ID INT AUTO_INCREMENT Primary_key,
            Name VARCHAR(100) not NULL,
            Age INT ,
            Gender varchar(20),
            time datetime
            )
                """
    cursor.execute(query)
    print(f"Table {table_name} created successfully.")


# function to add users
def add_user(name,age,gender,table_name,cursor):
    query = f""" 
            INSERT INTO {table_name} (name,age,gender)
            values(%s, %s, %s)
             """
    cursor.execute(query,(name,age,gender))
    db.commit()
    print("User assigned successfully!")










while(True):
    print(

        """
        1. Create Table for User Account 
        2. Add money to account ( insert ) : 
        3. view All transection of the account 
        4. 


        """
    )
    





#function to add income 
    
