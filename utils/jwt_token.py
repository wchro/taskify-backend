import jwt
import asyncio
from datetime import datetime, timedelta

SECRET_KEY = "yOQ}/tu7|5MO" # ‼️ Change later (env)

async def generate(user_id, exp):
    exp_date = datetime.now() + exp
    exp = int(exp_date.timestamp())

    payload = {
        "user_id": user_id,
        "exp": exp
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

async def get_tokens(user_id):
    session_token = asyncio.create_task(generate(user_id, timedelta(days=7)))
    access_token = asyncio.create_task(generate(user_id, timedelta(minutes=15)))
    tokens = await asyncio.gather(session_token, access_token)
    return tokens


def verify(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        if "user_id" in payload:
            user_id = payload["user_id"]
            return user_id
    except:
        return None
    