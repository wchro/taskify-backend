import jwt
from datetime import datetime

SECRET_KEY = "yOQ}/tu7|5MO" # ‼️ Change later (env)

def generate(user_id):
    payload = {
        "user_id": user_id,
        "datetime": int(datetime.now().timestamp())
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

def verify(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        if "user_id" in payload:
            user_id = payload["user_id"]
            return user_id
    except:
        return None
    