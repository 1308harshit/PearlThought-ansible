# from flask import Flask
# import mysql.connector
# import os

# app = Flask(__name__)

# # Database configuration from environment variables
# db_config = {
#     'host': os.getenv('DB_HOST', 'mysql'),
#     'database': os.getenv('DB_NAME', 'helloWorldDb'),
#     'user': os.getenv('DB_USER', 'root'),
#     'password': os.getenv('DB_PASS', 'MySQL@123')
# }

# @app.route('/')
# def hello():
#     return "Hello, World! Visit /db to test the MySQL connection."

# @app.route('/db')
# def test_db():
#     try:
#         # Connect to MySQL
#         conn = mysql.connector.connect(**db_config)
#         cursor = conn.cursor()

#         # Create a table (if it doesn't exist)
#         cursor.execute("""
#             CREATE TABLE IF NOT EXISTS test_table (
#                 id INT AUTO_INCREMENT PRIMARY KEY,
#                 message VARCHAR(255)
#             )
#         """)

#         # Insert a test record
#         cursor.execute("INSERT INTO test_table (message) VALUES ('Hello from Flask!')")
#         conn.commit()

#         # Fetch the record
#         cursor.execute("SELECT message FROM test_table WHERE message = 'Hello from Flask!'")
#         result = cursor.fetchone()

#         cursor.close()
#         conn.close()

#         return f"Database connection successful! Fetched record: {result[0]}"
#     except mysql.connector.Error as err:
#         return f"Failed to connect to MySQL: {err}"

# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=5000)


# ----------------------------------------------------------------------

from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

# Database configuration from environment variables
db_config = {
    'host': os.getenv('DB_HOST', 'host.docker.internal'),  
    'database': os.getenv('DB_NAME', 'helloWorldDb'),
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASS', 'MySQL@123')
}

@app.route('/')
def hello():
    return "Hello, World! Visit /db to test the MySQL connection."

@app.route('/db')
def test_db():
    try:
        # Connect to MySQL
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Create a table (if it doesn't exist)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS test_table (
                id INT AUTO_INCREMENT PRIMARY KEY,
                message VARCHAR(255)
            )
        """)

        # Insert a test record
        cursor.execute("INSERT INTO test_table (message) VALUES ('Hello from Flask!')")
        conn.commit()

        # Fetch the record
        cursor.execute("SELECT message FROM test_table WHERE message = 'Hello from Flask!'")
        result = cursor.fetchone()

        cursor.close()
        conn.close()

        return f"Database connection successful! Fetched record: {result[0]}"
    except mysql.connector.Error as err:
        return f"Failed to connect to MySQL: {err}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)