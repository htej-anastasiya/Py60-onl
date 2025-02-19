from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

engine = create_engine("postgresql://nastya@localhost/testdb2")

class DataBaseSessionManager:
    engine = engine

    def __enter__(self):
        self.db_session = Session(bind=self.engine)
        return self.db_session

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.db_session.rollback()
        else:
            self.db_session.commit()
        self.db_session.close()