from fastapi import FastAPI
from database import db, password as pswrd


app = FastAPI()

@app.post("/signup")
async def signup(username, password):
    if not db.check_if_exists("users", "username", username):
        password = pswrd.gen_hash(password.encode("UTF-8"))
        db.signup(username, password)
        return {"success": True, "msg": "You have successfully registered."}
    else:
        return {"success": False, "msg": "Sorry, that username is already taken. Please try another."}
