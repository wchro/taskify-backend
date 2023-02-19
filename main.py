from fastapi import FastAPI, Form
from services import auth
from utils import jwt_token, password as pswrd
from database import db


app = FastAPI()

@app.post("/user/login")
async def login(username: str = Form(), password: str = Form()):
    try:
        user = db.get_data("users", "username", username)
        user_id = user[0]
        password_hashed = user[2]
        if pswrd.check_pswd(password.encode("UTF-8"), password_hashed):
            tokens = await jwt_token.get_tokens(user_id)
            session_token = tokens[0]
            access_token = tokens[1]
            return {"success": True, "session_token": session_token, "access_token": access_token}
        else:
            return {"success": False, "msg": "Username or password is incorrect. Please try again."}
    except:
        return {"success": False, "msg": "Username or password is incorrect. Please try again."}
    
@app.post("/user/register")
async def register(username: str = Form(), password: str = Form()):
    return auth.register(username, password)
