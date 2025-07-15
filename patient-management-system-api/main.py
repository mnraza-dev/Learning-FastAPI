import json
from fastapi import FastAPI
app = FastAPI()


def load_data():
    with open('patients.json','r') as f:
        data = json.load(f)
    return data

@app.get("/")
async def index():
    return{
        "message":"Hi there"
    }
@app.get("/view")
async def view():
    data = load_data()
    return data