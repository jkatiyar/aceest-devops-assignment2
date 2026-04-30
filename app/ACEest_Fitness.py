from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
DB_NAME = "fitness.db"


# -----------------------------
# DATABASE SETUP
# -----------------------------
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS members (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            plan TEXT
        )
    """)
    conn.commit()
    conn.close()


# -----------------------------
# HOME ROUTE
# -----------------------------
@app.route('/')
def home():
    return jsonify({"message": "Welcome to ACEest Fitness API"})


# -----------------------------
# FORM UI (Browser Testing)
# -----------------------------
@app.route('/add_member_form')
def add_member_form():
    return '''
        <h2>Add Member</h2>
        <form method="POST" action="/add_member">
            Name: <input type="text" name="name"><br><br>
            Age: <input type="number" name="age"><br><br>
            Plan: <input type="text" name="plan"><br><br>
            <input type="submit" value="Add Member">
        </form>
    '''


# -----------------------------
# ADD MEMBER (POST)
# -----------------------------
@app.route('/add_member', methods=['POST'])
def add_member():
    if request.is_json:
        data = request.get_json()
        name = data.get('name')
        age = data.get('age')
        plan = data.get('plan')
    else:
        name = request.form.get('name')
        age = request.form.get('age')
        plan = request.form.get('plan')

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO members (name, age, plan) VALUES (?, ?, ?)",
        (name, age, plan)
    )
    conn.commit()
    conn.close()

    return jsonify({"message": "Member added successfully"}), 201


# -----------------------------
# GET MEMBERS
# -----------------------------
@app.route('/members', methods=['GET'])
def get_members():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM members")
    rows = cursor.fetchall()
    conn.close()

    members = []
    for row in rows:
        members.append({
            "id": row[0],
            "name": row[1],
            "age": row[2],
            "plan": row[3]
        })

    return jsonify({"members": members})


# -----------------------------
# MAIN
# -----------------------------
if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)