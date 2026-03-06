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
    def get_all_products(self):
        self._cursor.execute("SELECT * FROM product")
        products = self._cursor.fetchall()
        return products
    def insert_product(self, id, name, desc, price, quant, id_cat):
        request = "INSERT INTO product (id, name, description, price, quantity, id_category) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (id, name, desc, price, quant, id_cat)
        self._cursor.execute(request, values)
        self._db_connect.commit()

db = Database()
print(db.get_all_products())
db.close_db()