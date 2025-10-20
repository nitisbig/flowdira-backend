from pydantic import BaseModel
from sqlalchemy.orm import Session
from db.session import get_db
from fastapi import APIRouter, Depends
from services.auth_services import login_user

router = APIRouter(prefix='/auth', tags=['Auth'])

class LoginRequest(BaseModel):
    email: str
    password: str

@router.post('/login')
def login(data: LoginRequest, db: Session = Depends(get_db)):
    return login_user(db, data.email, data.password)
