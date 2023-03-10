from fastapi import FastAPI, Form
from services import auth, tasks
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
    return jwt_token.update_token(session_token)
    
@app.post("/token/invalidate")
async def invalidate_token(token = Form()):
    return jwt_token.invalidate(token)

@app.get("/tasks")
async def get_tasks(token = Form()):
    return tasks.get_tasks(token)

@app.post("/tasks/add")
async def add_tasks(title: str = Form(), description: str = Form(), date = Form(), token = Form()):
    return tasks.add_tasks(title, description, date, token)

@app.delete("/tasks/delete")
async def delete_tasks(task_id = Form(), token = Form()):
    return tasks.delete_tasks(task_id, token)

@app.patch("/tasks/update")
async def update_tasks(task_id = Form(), title = Form(), description = Form(), date = Form(), token = Form()):
    return tasks.update_tasks(task_id, title, description, date, token)

@app.post("/tasks/complete")
async def complete_tasks(task_id = Form(), complete = Form(), token = Form()):
    return tasks.complete_tasks(task_id, complete, token)


