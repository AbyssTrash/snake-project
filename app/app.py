from flask import Flask, render_template, request, jsonify
import mysql.connector
import os
app = Flask(__name__)

# Database Configuration
db_config = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD', 'password'),
    'database': os.getenv('DB_NAME', 'snake_game')
}

# Serve the game frontend
@app.route('/')
def index():
    return render_template('index.html')

# API to submit a score
@app.route('/submit_score', methods=['POST'])
def submit_score():
    data = request.json
    name = data['name']
    score = data['score']
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO leaderboard (name, score) VALUES (%s, %s)", (name, score))
    conn.commit()
    cursor.close()
    conn.close()
    return '', 200

# API to fetch the leaderboard
@app.route('/leaderboard', methods=['GET'])
def leaderboard():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT name, score FROM leaderboard ORDER BY score DESC LIMIT 10")
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
