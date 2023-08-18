from fastapi import HTTPException,Depends,APIRouter,status
from app.database.connection import create_connection
from app.database.user_operations import search_user
from ..utils import valid_password
from ..oauth2 import create_token
from fastapi.security import OAuth2PasswordRequestForm
from ..schemas.schemas import Token
router = APIRouter(prefix='/login',tags=['Authentication'])
@router.post('/',response_model=Token)
def login_user(user:OAuth2PasswordRequestForm = Depends(),conn = Depends(create_connection)):
    get_user = search_user(conn=conn,user=user)
    if not get_user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail='Invalid Credentials')
    if not valid_password(user=user,db_password=get_user['user_password']):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail='Invalid Credentials')
    token = create_token({'id':get_user['user_id']})
    return {'token':token,'token_type':'Bearer'}