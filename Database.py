import mysql.connector
import os 
import dotenv

class Database:
    def __init__(self):
        
        dotenv.load_dotenv()
        self._db_connect = mysql.connector.connect(
            host = os.getenv("DB_HOST"),
            user = os.getenv("DB_USER"),
            password = os.getenv("DB_PASSWORD"),
            db = os.getenv("DB_NAME")
        )   

        self._cursor = self._db_connect.cursor()

    def close_db(self):
        self._cursor.close()
        self._db_connect.close()


db = Database()
db.close_db()