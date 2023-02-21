from database import db
import jwt
from datetime import datetime, timedelta

SECRET_KEY = "yOQ}/tu7|5MO" # ‼️ Change later (env)

def generate(user_id, exp):
    exp_date = datetime.now() + exp
    exp = int(exp_date.timestamp())

    payload = {
        "user_id": user_id,
        "exp": exp
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

def verify(token):
    try:
        if not db.check_if_exists("invalid_tokens", "token", token):
            payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            if "user_id" in payload:
                user_id = payload["user_id"]
                return {"success": True, "user_id": user_id}
        else:
            return {"success": False, "msg": "Session expired. Please log in again to continue."}
    except:
        return {"success": False, "msg": "Session expired. Please log in again to continue."}
    
def generate_tokens(user_id):
    session_token = generate(user_id, timedelta(days=7))
    access_token = generate(user_id, timedelta(minutes=15))
    return {"success": True, "session_token": session_token, "access_token": access_token}

def invalidate(token):
    db.insert("INSERT INTO invalid_tokens (token, date_added) VALUES (?, ?)", (token, int(datetime.now().timestamp())))
    return {"success": True}
        