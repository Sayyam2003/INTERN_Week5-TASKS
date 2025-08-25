from flask import Flask, g
import sqlite3

app = Flask(__name__)
DATABASE = 'users.db'

# --- Database Connection Helper ---
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

# --- Create Table and Insert 3 Users ---
def init_db():
    conn = get_db()
    cursor = conn.cursor()
    
    # Create table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')
    
    # Check if users already exist
    cursor.execute('SELECT COUNT(*) FROM users')
    if cursor.fetchone()[0] == 0:
        # Insert 3 users
        cursor.executemany('INSERT INTO users (name) VALUES (?)', [
            ('Alice',), ('Bob',), ('Charlie',)
        ])
        conn.commit()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# --- Route to Fetch and Print Users ---
@app.route('/users')
def list_users():
    init_db()
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT name FROM users')
    users = cursor.fetchall()
    
    output = '<h2>Users:</h2><ul>'
    for user in users:
        output += f'<li>{user[0]}</li>'
    output += '</ul>'
    return output

if __name__ == '__main__':
    app.run(debug=True)
