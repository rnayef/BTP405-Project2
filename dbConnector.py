import mysql.connector

def mysqlConnection():
    """
    Establishes a connection with the MySQL database and returns a MySQL Connection Object
    """
    try:
        # Connect to MySQL database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="my_root_password",
            database="my_database"
        )
        print("[SERVER]: Successfully connected to MySQL database!")
        return connection
    except mysql.connector.Error as err:
        print(f"[ERROR]: {err}")
        return None

def closeConnection(connection):
    """
    Closes the connection with the MySQL database
    """
    try:
        if connection.is_connected():
            connection.close()
            print("[SERVER]: MySQL connection closed!")
    except mysql.connector.Error as err:
        print(f"[ERROR]: {err}")


