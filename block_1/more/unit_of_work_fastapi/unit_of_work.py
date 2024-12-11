from db import SessionLocal
from repositories import UserRepository


class UnitOfWork:
    def __init__(self):
        self.session = SessionLocal()

    def __enter__(self):
        self.user_repository = UserRepository(self.session)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            self.rollback()
        self.session.close()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
