from fastapi import FastAPI
from database import db, password as pswrd


app = FastAPI()

@app.post("/signup")
async def signup(username, password):
    password = pswrd.gen_hash(password.encode("UTF-8"))
    db.signup(username, password)
    return {"success": True, "msg": "You have successfully registered."}
