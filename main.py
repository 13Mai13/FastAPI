from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True  # Default value
    rating: Optional[int] = None

my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1}]


@app.get("/")
async def root():
    return {'message': 'Hello World v2'}


@app.get("/posts")
async def get_posts():
    return {"data": "This is your posts"}


@app.post("/posts")
async def create_posts(new_post: Post):
    print(new_post.published, new_post.rating)
    return {"data": "data"}