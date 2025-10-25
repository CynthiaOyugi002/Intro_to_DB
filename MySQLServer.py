"""
This script creates the database 'alx_book_store' in the MySQL server.
If the database already exists, the script will not fail.
"""

import mysql.connector
from mysql.connector import Error

try:
    
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="9614Cream!363"
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except Error as e:
    print(f"Error while connecting to MySQL: {e}")

finally:
    try:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")
    except NameError:
        print("Connection was never established.")
