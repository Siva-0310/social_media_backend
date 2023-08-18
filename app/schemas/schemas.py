from pydantic import BaseModel,EmailStr
from typing import List,Optional
from datetime import datetime
class UserRegister(BaseModel):
    user_email:EmailStr
    user_password:str
    user_name:str
class Token(BaseModel):
    token:str
    token_type:str
    class Config:
        from_attributes = True
class TokenDecode(BaseModel):
    id:int
class PostOut(BaseModel):
    post_id:int
    post_text:str
    post_date_time:datetime
    post_votes:int
    class Config:
        from_attributes = True
class PostsOut(BaseModel):
    posts:List[PostOut]
    class Config:
        from_attributes = True
class Post(BaseModel):
    post_text:str
    post_votes:int = 0
class SinglePostOut(PostOut):
    user_id:int
class UpdatePosts(BaseModel):
    text:str