from fastapi import APIRouter,HTTPException,status,Depends
from ..database.connection import create_connection
from ..database.posts_operations import get_posts,create_posts,get_post,delete_post,update_post,increment_votes
from ..schemas.schemas import PostOut,SinglePostOut,Post,TokenDecode,PostsOut,UpdatePosts
from ..oauth2 import get_user
router = APIRouter(prefix='/posts',tags=['Posts'])
@router.get("/",status_code=status.HTTP_200_OK,response_model=PostsOut)
def get_users(conn = Depends(create_connection)):
    data = get_posts(conn)
    if(len(data) == 0):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Data not found")
    json_data = {}
    json_data['posts'] = data
    return json_data
@router.post("/",status_code=status.HTTP_201_CREATED,response_model=PostOut)
def create_users(post:Post,conn = Depends(create_connection),id:TokenDecode = Depends(get_user)):
    new_post = create_posts(conn=conn,post=post,id=id)
    if new_post == 'Invalid User':
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail='Login to create post')
    return new_post
@router.get("/{post_id}",status_code=status.HTTP_200_OK,response_model=SinglePostOut)
def get_single_post(post_id:int,conn = Depends(create_connection)):
    data = get_post(conn=conn,post_id=post_id)
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    if data == 'error':
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail='Server error')
    return data
@router.delete("/{post_id}",status_code=status.HTTP_204_NO_CONTENT)
def post_delete(post_id:int,conn=Depends(create_connection),id:TokenDecode = Depends(get_user)):
    operation_result = delete_post(conn=conn,post_id=post_id,user_id=id.id)
    if operation_result == 'Not Found':
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Post dont exists')
    elif operation_result == 'Not Autherize':
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail='Not Autherize')
    elif operation_result:
        return {"message":"it is deleted"} 
@router.put("/{post_id}",response_model=PostOut,status_code=status.HTTP_201_CREATED)
def posts_update(post_id:int,text:UpdatePosts,conn = Depends(create_connection),id:TokenDecode = Depends(get_user)):
    data = update_post(post_id=post_id,text=text,user_id=id.id,conn=conn)
    if data == 'Post dont exists':
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=data)
    if data == 'Not Autherize':
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=data)
    return data
@router.put("/votes/{post_id}",response_model=PostOut,status_code=status.HTTP_201_CREATED)
def increase_votes(post_id:int,conn = Depends(create_connection),id:TokenDecode = Depends(get_user)):
    data = increment_votes(post_id=post_id,conn=conn)
    if data == 'Post dont exists':
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=data)
    return data  