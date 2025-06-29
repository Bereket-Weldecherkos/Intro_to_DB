# MySQLServer.py

import mysql.connector
from mysql.connector import errorcode

def create_database():
    try:
        # Connect to MySQL server
        conn = mysql.connector.connect(
            host="localhost",       # Replace with your host
            user="root",            # Replace with your MySQL username
            password="your_password"  # Replace with your MySQL password
        )

        cursor = conn.cursor()

        # Attempt to create database
        try:
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
        except mysql.connector.Error as err:
            print(f"Failed creating database: {err}")

        # Close the cursor and connection
        cursor.close()
        conn.close()

    except mysql.connector.Error as err:
        print(f"Error: Could not connect to MySQL server.\nDetails: {err}")

if __name__ == "__main__":
    create_database()
