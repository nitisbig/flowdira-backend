from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from services.user_service import get_user_by_email
from core.security import verify_password, generate_token

def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    if not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid Credintials')
    
    return user

def login_user(db: Session, email: str, password: str):
    user = authenticate_user(db, email, password)
    access_token = generate_token(data={"sub": str(user.id), 'email': user.email})
    return {"access_token": access_token, "token_type":'bearer'}