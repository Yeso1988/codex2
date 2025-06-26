import mysql.connector
from mysql.connector import errorcode

# Configure your MySQL connection settings
DB_CONFIG = {
    'user': 'root',
    'password': 'password',  # replace with your MySQL root password
    'host': 'localhost',
    'database': 'info_db'
}

TXT_FILE = 'info.txt'


def record_to_file(data, filename=TXT_FILE):
    """Append the provided data to a text file."""
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(data + "\n")


def init_database():
    """Create the database and table if they do not exist."""
    connection = mysql.connector.connect(user=DB_CONFIG['user'],
                                         password=DB_CONFIG['password'],
                                         host=DB_CONFIG['host'])
    cursor = connection.cursor()
    try:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_CONFIG['database']}")
        connection.database = DB_CONFIG['database']
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS entries (
                id INT AUTO_INCREMENT PRIMARY KEY,
                content TEXT NOT NULL
            )
            """
        )
        connection.commit()
    finally:
        cursor.close()
        connection.close()


def store_in_mysql(data):
    """Store the provided data in the MySQL database."""
    connection = mysql.connector.connect(**DB_CONFIG)
    cursor = connection.cursor()
    try:
        cursor.execute("INSERT INTO entries (content) VALUES (%s)", (data,))
        connection.commit()
    finally:
        cursor.close()
        connection.close()


def read_from_mysql():
    """Retrieve all data from the MySQL database."""
    connection = mysql.connector.connect(**DB_CONFIG)
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT id, content FROM entries")
        rows = cursor.fetchall()
        for row in rows:
            print(f"{row[0]}: {row[1]}")
    finally:
        cursor.close()
        connection.close()


def main():
    init_database()
    data = input("Enter information to store: ")
    record_to_file(data)
    store_in_mysql(data)
    print("\nCurrent stored entries:")
    read_from_mysql()


if __name__ == '__main__':
    main()
