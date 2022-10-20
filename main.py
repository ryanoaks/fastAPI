from fastapi import FastAPI

app = FastAPI()


#path operation/route
#
@app.get("/")
def root():
    return {"message": "Hello"}

@app.get("/post")
def get_posts():
    return {"data": "This is your post"}