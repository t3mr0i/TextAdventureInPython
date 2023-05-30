import sqlite3

def create_database():
    # Connect to the SQLite database
    conn = sqlite3.connect('game.db')
    c = conn.cursor()

    # Create table for characters
    c.execute('''
        CREATE TABLE IF NOT EXISTS characters (
            name TEXT,
            introduction TEXT,
            memory TEXT
        )
    ''')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

# Call the function to create the database
create_database()
