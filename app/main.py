from fastapi import FastAPI

import sys
sys.path.append(".\\")
import models
from api import items, users
from database import engine


app = FastAPI()

app.include_router(users.router, tags=['users'])
app.include_router(items.router, tags=['items'])