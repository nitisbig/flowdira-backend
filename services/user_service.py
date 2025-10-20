from sqlalchemy.orm import Session
from models.user import User
from schemas.user import UserCreate
from core.security import generate_hash

def create_user(db: Session, user_data: UserCreate) -> User:
    hashed_pwd = generate_hash(user_data.password)
    user = User(
        name = user_data.name,
        email= user_data.email,
        password = hashed_pwd
    )
    db.add(user)
    db.commit()
    return user

def get_user_by_id(db: Session, user_id: int) -> User | None:
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_email(db: Session, email: str) -> User |None:
    return db.query(User).filter(User.email == email).first()