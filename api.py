import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

api = FastAPI()

class User(BaseModel):
    username:str
    password:str
    age:int|None

@api.get("/")
def main():
    return {"Msg":"This is main"}

@api.get("/auth")
def auth():
    return {"Msg":"this is the auth endpoint"}

@api.post("/auth/login")
def login(user:User):
    return {"Msg":"this is the login endpoint"}

@api.post("/auth/sign-up")
def sign_up(user:User):
    return {"Msg":"this is the sign-up endpoint"}



if __name__ == "__main__":
    uvicorn.run(api)