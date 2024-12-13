from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

@app.get("/")
async def welcome() -> str:
    return "Главная страница"

@app.get("/user/{username}/{age}")
async def user_predator(username: Annotated[str, Path(min_length = 5, max_length = 20, description="Enter username", example = 'UrbanUser')]
                        , age: int = Path(ge=18, le=120, description="Enter age", example=24)) -> dict:
    return {"Информация о пользователе:" "Имя": username, "Возраст": age}

@app.get("/user/admin")
async def welcome_admin() -> str:
    return "Вы вошли как администратор"

@app.get("/user/{user_id}")
async def welcome_user(user_id: int = Path(ge=1, le=100, description="Enter User ID", examples=69)) -> dict:
    return {f"Вы вошли как пользователь № {user_id}"}
