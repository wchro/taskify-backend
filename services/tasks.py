from database import db
from services.auth import jwt_token

def get_tasks(token):
    user = jwt_token.verify(token)
    if user["success"] and user["access"]:
        tasks = db.get_data("tasks", "user_id", user["user_id"], True)
        json = {"success": True, "tasks": []}
        if tasks:
                for task in tasks:
                     json_task = {
                          "id": task[0],
                          "title": task[1],
                          "description": task[2],
                          "date": task[3],
                          "completed": task[4]
                     }
                     json["tasks"].append(json_task)
        return json
    else:
        return {"success":False, "msg": "Please provide valid credentials."}
    
def add_tasks(title, description, date, token):
    user = jwt_token.verify(token)
    if user["success"]:
        user_id = user["user_id"]
        db.insert("INSERT INTO tasks (title, description, date, completed, user_id) VALUES (?,?,?,?, ?)", (title, description, date, 0, user_id))
        return {"success": True, "msg": "Task added successfully!"}
    else:
        return {"success": False, "msg": "Please provide valid credentials."}