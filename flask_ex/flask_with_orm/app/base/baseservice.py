from app.base.db_connection import SessionLocal

class BaseService:
    def __init__(self, db = None):
        self._db=db or SessionLocal()


    def add_to_session(self, obj):
        self._db.add(obj)

    def delete_from_session(self, obj):
        self._db.delete(obj)

    def refresh_obj(self, obj):
        self._db.refresh(obj)

    def commit(self):
        self._db.commit()

    def query(self, model_name):
        return self._db.query(model_name)

