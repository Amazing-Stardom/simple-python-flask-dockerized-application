from flask import Flask
import psycopg2
import os

app = Flask(__name__)

db_host = os.environ.get('DB_HOST')
db_name = os.environ.get('DB_NAME')
db_user = os.environ.get('DB_USER')
db_pass = os.environ.get('DB_PASSWORD')

@app.route('/')
def check_db():
    try:
        conn = psycopg2.connect(
            host=db_host,
            dbname=db_name,
            user=db_user,
            password=db_pass
        )
        conn.close()
        return "Success! Connected to the PostgreSQL database."
    except psycopg2.OperationalError as e:
        return f"Connection failed: {e}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)