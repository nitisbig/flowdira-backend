import bcrypt
from datetime import datetime, timedelta
from jose import JWTError, jwt

def generate_hash(password: str) -> str:
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def verify_password(password: str, hashed: str) -> bool:
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

#JWT config
SECRET_KEY = 'secretkey'
alogrithm = 'HS256'
Token_Expire_Duration = 60

def generate_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=Token_Expire_Duration))
    to_encode.update({'exp': expire})
    encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=alogrithm)
    return encode_jwt

def decode_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[alogrithm])
        return payload
    except JWTError:
        return None

