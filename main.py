from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {'message': 'Hello World v2'}


@app.get("/posts")
async def get_posts():
    return {"data": "This is your posts"}


@app.post("/createposts")
async def create_posts():
    return {"message": "Successfully created post"}