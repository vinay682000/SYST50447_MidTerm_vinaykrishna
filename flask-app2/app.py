from flask import Flask, request, jsonify
import psycopg2
import os

app = Flask(__name__)

# Database connection parameters from environment variables
DB_HOST = os.environ.get('DB_HOST', 'db')
DB_NAME = os.environ.get('DB_NAME', 'postgres')
DB_USER = os.environ.get('DB_USER', 'postgres')
DB_PASS = os.environ.get('DB_PASSWORD', 'postgres')

def get_db_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )
    return conn

@app.route('/')
def hello():
    return {"message": "Hello, Docker World!"}

@app.route('/init-db', methods=['POST'])
def init_db():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS messages (id SERIAL PRIMARY KEY, content TEXT);')
    conn.commit()
    cur.close()
    conn.close()
    return {"message": "Database initialized"}

@app.route('/message', methods=['POST'])
def add_message():
    content = request.json.get('content', '')
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO messages (content) VALUES (%s) RETURNING id;', (content,))
    id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return {"id": id, "content": content}

@app.route('/messages', methods=['GET'])
def get_messages():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT id, content FROM messages;')
    messages = [{"id": row[0], "content": row[1]} for row in cur.fetchall()]
    cur.close()
    conn.close()
    return jsonify(messages)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
EOF