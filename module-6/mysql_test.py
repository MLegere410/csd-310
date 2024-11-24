# Madison Legere, 11/23/2024, Module 6.2

import mysql.connector

# Create a connection to the MySQL database
db_config = {
    'user': 'root', 
    'password': 'Lm04102001!',
    'host': 'localhost', 
    'database': 'movies' 
}

try:
    connection = mysql.connector.connect(**db_config)
    print("Connection Successful!")
except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    if connection.is_connected():
        connection.close()
        print("Connection Closed")

