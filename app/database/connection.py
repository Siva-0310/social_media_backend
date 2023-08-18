import psycopg2
from psycopg2.extras import RealDictCursor
import time
from app.database.connection_details import HOST,PASSWORD,DATABASE,USER
def create_connection():
    while True:
        try:
            conn = psycopg2.connect(host=HOST,password=PASSWORD,database=DATABASE,user=USER,cursor_factory=RealDictCursor)
            return conn
        except Exception as error:
            print("Failed to connect to database",error)
            time.sleep(15)
