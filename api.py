import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from db import check_user_exixts

api = FastAPI()

class User(BaseModel):
    username:str
    password:str
    age:int|None

@api.get("/")
def main():
    return {"Msg":"This is main"}

@api.get("/auth")
async def auth(): #this is cool, I know what I'm doing
    return {"Msg":"this is the auth endpoint"}

@api.post("/auth/login")
async def login(user:User):
    return {"Msg":"this is the login endpoint"}

@api.post("/auth/sign-up")
async def sign_up(user:User):
    if check_user_exixts():
        print("I know!!!")
    return {"Msg":"this is the sign-up endpoint"}

@api.post("/query/{username}")
async def sign_up(username:int):
    if check_user_exixts():
        print("I know!!!")
    return {"Msg":"this is the sign-up endpoint"}

if __name__ == "__main__":
    uvicorn.run(api)