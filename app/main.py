from fastapi import FastAPI
from .routers import users,auth,posts
app = FastAPI()
app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)
@app.get('/')
def root():
    return {"message":"root"}