from flask import Flask, jsonify, render_template
from database import get_total_users, get_premium_users
import sqlite3
import os

app = Flask(__name__)

DB_PATH = os.path.join(os.path.dirname(__file__), "users.db")

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/stats')
def stats():
    total = get_total_users()
    premium = get_premium_users()
    return jsonify({
        "total_users": total,
        "premium_users": premium,
        "free_users": total - premium
    })

@app.route('/users')
def users():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT user_id, username, first_name, join_date, is_premium, ask_count FROM users')
    rows = cursor.fetchall()
    conn.close()
    users_list = []
    for row in rows:
        users_list.append({
            "user_id": row[0],
            "username": row[1],
            "first_name": row[2],
            "join_date": row[3],
            "is_premium": bool(row[4]),
            "ask_count": row[5]
        })
    return jsonify(users_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
