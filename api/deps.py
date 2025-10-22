from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from core.security import decode_token
from db.session import get_db
from services.user_service import get_user_by_id
outh2_cheme = OAuth2PasswordBearer(tokenUrl='/atuh/login')
def get_current_user(token: str=Depends(outh2_cheme), db: Session = Depends(get_db) ):
    payload = decode_token(token)
    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid or expired access token',
            headers={"WWW-Authenticate": "Bearer"}
        )
    user_id = payload.get('sub')
    if user_id is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='invalid payload')
    
    user = get_user_by_id(db, int(user_id))
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='user not found')
    
    return user
    
