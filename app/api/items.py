from typing import List

from fastapi import FastAPI, Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
import sys
sys.path.append("..\\")
import crud, models, schemas, deps

router = APIRouter()


@router.post('/users/{user_id}/items/', response_model=schemas.Item)
def create_item_for_user(user_id: int, item: schemas.ItemCreate, db: Session = Depends(deps.get_db)):
    return crud.create_user_item(db=db, item=item, user_id = user_id)


@router.get('/items/', response_model=schemas.Item)
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(deps.get_db)):
    items = crud.get_items(db, skip = skip, limit = limit)
    return items