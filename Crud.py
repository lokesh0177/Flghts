import mysql.connector

# connect to the database server

try:
    conn = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='Lokesh@123',
        database = 'indigo'

    )
    mycursor = conn.cursor()
    print('Connection establshed')

except mysql.connector.Error as e:
    print(e)

# mycursor.execute('CREATE DATABASE indigo')
# conn.commit

#create a table
# mycursor.execute("""
#     CREATE TABLE airport (airport_id INTEGER PRIMARY KEY,
#     code VARCHAR(10) NOT NULL,
#     city VARCHAR(50) NOT NULL,
#     name VARCHAR(255) NOT NULL
# )
# """
# )
# conn.commit()

#Insert Data Into Table
# mycursor.execute("""
#     INSERT INTO airport VALUES
#     (1,'DEL','New Delhi','IGTA'),
#     (2,'CCU','Kolkata','NSCA'),
#     (3,'BOM','Mumbai','CSMA')
#
# """)
#
# conn.commit()

#SEARCH
mycursor.execute('SELECT * FROM airport WHERE airport_id  > 1')
data = mycursor.fetchall()
print(data)