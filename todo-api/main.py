from fastapi import FastAPI
app = FastAPI()

@app.get("/items")
def list_items():
    return {"message": "List of Items"}

@app.get("/items/{item_id}")
def get_items(item_id:int):
    return {
        "message":item_id
    }