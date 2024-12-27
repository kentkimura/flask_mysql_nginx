from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, Flask!"

@app.route("/db")
def test_db():
    try:
        conn = mysql.connector.connect(
            host="db",
            user="user",
            password="password",
            database="testdb"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT 'DB Connected!'")
        result = cursor.fetchone()
        conn.close()
        return result[0]
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)