from flask import Flask
import redis
import mysql.connector

app = Flask(__name__)

@app.route('/')
def index():
    # Redis
    r = redis.Redis(host='redis', port=6379, decode_responses=True)
    count = r.incr('counter')

    # MySQL
    conn = mysql.connector.connect(
        host="mysql",
        user="user",
        password="password",
        database="testdb"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sample")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    return f"Redis Count: {count}<br>MySQL Data: {rows}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)