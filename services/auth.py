from database import db
from utils import password as pswrd

def login(username: str, password: str):
    user = db.get_data("users", "username", username)
    password_hashed = user[2]
    if pswrd.check_pswd(password.encode("UTF-8"), password_hashed):
        return {"success": True}
    else:
        return {"success": False}

def register(username: str, password: str):
    if not db.check_if_exists("users", "username", username):
        password = pswrd.gen_hash(password.encode("UTF-8"))
        db.insert("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        return {"success": True, "msg": "You have successfully registered."}
    else:
        return {"success": False, "msg": "Sorry, that username is already taken. Please try another."}

