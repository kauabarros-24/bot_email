from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from src.bot_email.database import engine, get_db, Base
from src.bot_email.schemas import UserCreate, UserResponse 
from src.bot_email.models import User
from fastapi import FastAPI, Depends, HTTPException, status

app = FastAPI()
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "System running!"}

@app.post("/users/", response_model=UserResponse)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Este e-mail já está cadastrado. Por favor, utilize outro."
        )
    
    if len(user.password) < 8:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="A senha deve ter pelo menos 8 caracteres."
        )
    
    hashed_password = User.hash_password(password=user.password)

    db_user = User(name=user.name, email=user.email, password=hashed_password)
    db.add(db_user)
    try:
        db.commit()
        db.refresh(db_user)
        return {"message": "User created with successfully", "id": str(db_user.id), "name": db_user.name, "email": db_user.email}
    except Exception as e:
        db.rollback()
        raise HTTPException(
            data=str(e),
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ocorreu um erro ao tentar criar o usuário. Tente novamente mais tarde."
        )
    







