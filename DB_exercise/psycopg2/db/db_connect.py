import psycopg2
from db.config import DB_CONFIG

class DbConnection:
    def __enter__(self):
        self.connect_db = psycopg2.connect(**DB_CONFIG)
        self.cursor = self.connect_db.cursor()
        # print(f" __enter__ возвращает: {type(self.cursor)}")
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.connect_db.rollback() #return back changes
        else:
            self.connect_db.commit()
        self.cursor.close()
        self.connect_db.close()

# with DbConnection() as cursor:
#     print(f"Проверка: {type(cursor)}")