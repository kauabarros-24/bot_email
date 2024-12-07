from sqlalchemy import Column, Integer, String
from src.bot_email.database import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid
from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class User(Base):
    __tablename__ = "users"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4) 
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    
    def verify_password(password: str) -> bool:
        return pwd_context.verify(password)

    def hash_password(password: str) -> str:
        return pwd_context.hash(password)   
    