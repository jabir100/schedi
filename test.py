import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('teams.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Now you can execute SQL commands using the cursor

# For example, you can query data from the database
cursor.execute('SELECT * FROM teams')
teams = cursor.fetchall()
print("Teams:", teams)

# Once you're done with database operations, remember to close the connection
conn.close()
