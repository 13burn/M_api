import uvicorn
from fastapi import FastAPI

api = FastAPI()

@api.get("/")
def main():
    return {"Msg":"This is main"}

if __name__ == "__main__":
    uvicorn.run(api)