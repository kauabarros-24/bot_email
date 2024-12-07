from sqlalchemy.orm import Session
from src.bot_email.models import User
from src.bot_email.schemas import UserCreate
from hashlib import sha256


def create_user(db: Session, user: UserCreate):
    hashed_password = sha256(user.password.encode('utf-8')).hexdigest()
    db_user = User(name=user.name, email=user.email, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user