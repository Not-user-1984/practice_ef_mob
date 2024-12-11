from sqlalchemy.orm import Session
from models import User
from schemas import UserCreate


class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def create_user(self, user: UserCreate):
        db_user = User(name=user.name, email=user.email)
        self.session.add(db_user)
        return db_user

    def get_user(self, user_id: int):
        return self.session.query(User).filter(User.id == user_id).first()
