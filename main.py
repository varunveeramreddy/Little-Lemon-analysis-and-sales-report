import mysql.connector
from mysql.connector import pooling
dbconfig = {
    "user": "your_user",
    "password": "your_password",
    "host": "localhost",
    "database": "LittleLemonDB"
}

connection_pool = mysql.connector.pooling.MySQLConnectionPool(pool_name="mypool",
                                                              pool_size=5,
                                                              **dbconfig)
print("Connection pool created successfully.")
#Example SQL to create database
create_database_query = "CREATE DATABASE IF NOT EXISTS LittleLemonDB"
create_table_query = """
CREATE TABLE IF NOT EXISTS Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY,
    FullName VARCHAR(100),
    PhoneNumber VARCHAR(15),
    Email VARCHAR(100)
);
"""
connection = connection_pool.get_connection()
cursor = connection.cursor()
cursor.callproc("GetAllCustomers")

for result in cursor.stored_results():
    print(result.fetchall())

cursor.close()
connection.close()
connection.close()
print("Connection returned to the pool.")
