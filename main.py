from fastapi import FastAPI, Form
from services import auth
from utils import password as pswrd


app = FastAPI()

@app.post("/user/login")
async def login(username: str = Form(), password: str = Form()):
    return auth.login(username, password)


@app.post("/user/register")
async def register(username: str = Form(), password: str = Form()):
    return auth.register(username, password)
