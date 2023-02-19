from fastapi import FastAPI, Form
from services import auth
from utils import jwt_token, password as pswrd


app = FastAPI()

@app.post("/user/login")
async def login(username: str = Form(), password: str = Form()):
    if auth.login(username, password):
        tokens = await jwt_token.get_tokens(1)
        session_token = tokens[0]
        access_token = tokens[1]
        return {"success": True, "session_token": session_token, "access_token": access_token}
    else:
        return {"success": False, "msg": "Username or password is incorrect. Please try again."}
    
@app.post("/user/register")
async def register(username: str = Form(), password: str = Form()):
    return auth.register(username, password)
