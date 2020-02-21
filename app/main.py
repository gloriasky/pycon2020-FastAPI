from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/users/{user_id}")
def read_item(user_id: int):
    return {"item_id": user_id, "email": "john.doe@example.com"}