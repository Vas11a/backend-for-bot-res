from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
import os

app = FastAPI()
port = int(os.environ.get("PORT", 8000))


data = [{"country": "Ukraina", "data": "20202", "activity": "40404"}, {"country": "Poland", "data": "2000", "activity": "3434"}]

class Manual(BaseModel):
    code: str
    phone: str

@app.post("/register-manual")
def create_data(item: Manual):
    return {"message": "Акаунт добавлен мануально"}


class Auto(BaseModel):
    country: str
    amount: str

@app.post("/register-auto")
def create_data(item: Auto):
    return {"message": "Акаунт добавлен автоматически"}


class SemiAuto(BaseModel):
    code: str
    amount: str


@app.post("/register-semi-auto")
def create_data(item: SemiAuto):
    data.append(item)
    return {"message": "Акаунт добавлен полу автоматически"}


@app.get("/getList")
def get_data():
    return data

@app.get("/test")
def get_data():
    return 'Api is working'


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=port)
