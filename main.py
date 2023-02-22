from fastapi import FastAPI, Form
from services import auth
from utils import jwt_token, password as pswrd


app = FastAPI()

@app.post("/user/login")
async def login(username: str = Form(), password: str = Form()):
    return auth.login(username, password)

@app.post("/user/register")
async def register(username: str = Form(), password: str = Form()):
    return auth.register(username, password)

@app.get("/token/verify")
async def verify_token(token = Form()):
    return jwt_token.verify(token)

@app.put("/token/update")
async def update_token(session_token = Form()):
    user = jwt_token.verify(session_token)
    if user["success"]:
        return jwt_token.generate_tokens(user)
    else:
        return {"success": False, "msg": "Session expired. Please log in again to continue."}
    
@app.post("/token/invalidate")
async def invalidate_token(token = Form()):
    return jwt_token.invalidate(token)
