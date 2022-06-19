from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

@app.get("/")
async def root():
    return {'message': 'Hello World v2'}


@app.get("/posts")
async def get_posts():
    return {"data": "This is your posts"}


@app.post("/createposts")
async def create_posts(payLoad: dict = Body(...)):
    print(payLoad)
    return {"message": "Successfully created post"}