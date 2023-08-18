from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm
password_context = CryptContext(schemes=['bcrypt'],deprecated='auto')
def create_hash(password:str):
    return password_context.hash(password)
def valid_password(user:OAuth2PasswordRequestForm,db_password:str):
    return password_context.verify(user.password,db_password)