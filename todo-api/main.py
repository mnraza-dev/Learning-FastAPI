from fastapi import FastAPI
app = FastAPI()

@app.get("/about")
async def about():
    return{
        "message":"About me"
    }

@app.get("/users/{user_id}")
async def get_users(user_id:str):
    return {
        "message":user_id
    }
@app.get("/items")
async def list_items():
    return {"message": "List of Items"}

@app.get("/items/{item_id}")
async def get_items(item_id:int):
    return {
        "message":item_id
    }

@app.post("/")
async def create_form():
    return{
        "data":"All forms listed"
    }