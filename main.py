import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='your_password',
    database='LittleLemon'
)

cursor = connection.cursor()
print("Connected to the database successfully!")

cursor.callproc('AddBooking', (1, '2024-02-20'))
connection.commit()
