from sqlalchemy.orm import Session
from db.base import SessionLocal
from schemas.user import UserCreate, UserOut
from services.user_service import create_user
from fastapi import APIRouter, Depends

router = APIRouter(prefix='/users')

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post('/', response_model=UserOut)
def register_user(user_data: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user_data)

