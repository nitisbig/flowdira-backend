from sqlalchemy.orm import Session
from db.base import SessionLocal
from schemas.user import UserCreate, UserOut
from services.user_service import create_user
from fastapi import APIRouter, Depends
from db.session import get_db

router = APIRouter(prefix='/users')

@router.post('/', response_model=UserOut)
def register_user(user_data: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user_data)

