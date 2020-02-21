from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserCreate(BaseModel):
    email: str
    password: str

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/users/{user_id}")
def read_item(user_id: int):
    return {"item_id": user_id, "email": "john.doe@example.com"}


@app.post("/users")
def create_user(user: UserCreate):
    return user
