import mysql.connector
from mysql.connector import Error

def create_connection(host="localhost", user="root", password="password", database="cricsheet_db"):
    """Create a connection to MySQL database."""
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        if connection.is_connected():
            print("✅ Connected to MySQL database")
            return connection
    except Error as e:
        print(f"❌ Error: {e}")
        return None
