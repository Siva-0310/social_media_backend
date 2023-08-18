from jose import JWTError,jwt
from datetime import timedelta,datetime
from .schemas.schemas import TokenDecode
from fastapi import Depends,status,HTTPException
from fastapi.security import OAuth2PasswordBearer
oauth2_scheme = OAuth2PasswordBearer('login')
KEY = "c2JhNTd1bGJhaTVjdWxiYWo1c2JhNTd1bGJhaTVjdWxiYWo1"
ALGORITHM = "HS256"
EXPIRY_TIME_IN_MINUTES = 90
def create_token(data:dict):
    to_encode = data.copy()
    expiry = datetime.utcnow() + timedelta(minutes=EXPIRY_TIME_IN_MINUTES)
    to_encode['exp'] = expiry
    return jwt.encode(to_encode,KEY,algorithm=ALGORITHM)
def verify_token(token:str,httpexception):
    try:
        payload = jwt.decode(token,KEY,algorithms=[ALGORITHM])
        id:str = payload.get('id')
        if not id:
            raise httpexception
        token_decode = TokenDecode(id=id)
    except JWTError:
        raise httpexception
    return token_decode
def get_user(token:str = Depends(oauth2_scheme)):
    httpexception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='Could not validate user',headers={'WWW-Authenticate':'Bearer'})
    return verify_token(token=token,httpexception=httpexception)