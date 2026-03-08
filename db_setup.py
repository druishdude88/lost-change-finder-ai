import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
def initialize_db():
    connection = sqlite3.connect('claims.db')
    cursor = connection.cursor()

    # Create claims table
    cursor.execute('''CREATE TABLE IF NOT EXISTS claims (
        id INTEGER PRIMARY KEY,
        description TEXT NOT NULL,
        amount REAL NOT NULL,
        status TEXT NOT NULL
    )''')

    # Commit changes and close the connection
    connection.commit()
    connection.close()

if __name__ == '__main__':
    initialize_db()