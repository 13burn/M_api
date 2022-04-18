import uvicorn
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import Depends, FastAPI
from pydantic import BaseModel
from db import check_user_exixts, create_user

api = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class User(BaseModel):
    username:str
    password:str
    age:int|None

@api.get("/")
def main():
    return {"Msg":"This is main"}

@api.get("/auth")
async def auth(token:str=Depends(oauth2_scheme)): #this is cool, I know what I'm doing
    print(token)
    return {"Msg":"this is the auth endpoint"}

@api.post("/auth/sign-up")
async def sign_up(user:User):
    if check_user_exixts(user.username):
        return{"Status":"Error", "Msg":"Cannot create user, name already exists"}
    else:
        create_user(user.username, user.password,user.age)
        return{"Status":"Success", "Msg":"Username creatd!"}

@api.post("/query/{username}")
async def query(username:str):
    if check_user_exixts(username):
        return{"Status":"Error", "Msg":"Cannot create user, name already exists"}
    else:
        return{"Status":"Success", "Msg":"This username is available"}
 
@api.post("/token")
async def token(form_data:OAuth2PasswordRequestForm = Depends()):
    print(form_data)
    return {"access_token":form_data.username+"token"}


if __name__ == "__main__":
    uvicorn.run(api)
