from fastapi import status,HTTPException,APIRouter,Depends
from ..schemas.schemas import UserRegister,Token
from ..database.connection import create_connection
from .. import utils
from app.database.user_operations import register_user
from ..oauth2 import create_token
router = APIRouter(prefix='/users',tags=['Users'])
@router.post('/',response_model=Token,status_code=status.HTTP_201_CREATED)
def create_user(user:UserRegister,conn = Depends(create_connection)):
    if len(user.user_password) < 8:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail='password length is less than 8 characters')
    user.user_password = utils.create_hash(user.user_password)
    new_user = register_user(conn=conn,user_register=user)
    if new_user == 'UniqueViolation':
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail='User is already exists with this email or user name')
    if new_user == 'CheckViolation':
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail='password length is less than 8 characters')
    token = create_token({'id': new_user['user_id']}) 
    return {'token':token,'token_type':'Bearer'}