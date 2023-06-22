from fastapi import APIRouter, Depends, HTTPException, status

from services import item_service

from models import item_dto

from sqlalchemy.orm import Session
from database.database import SessionLocal


router = APIRouter(
    prefix="/item",
    tags=["Item"],
    responses={404: {"description": "Not found"}},
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
def get_items(skip: int = 0, limit: int = 1000, db: Session = Depends(get_db)):
    items = item_service.get_items(db, skip=skip, limit=limit)
    return items


@router.get("/{item_id}")
def get_item_by_id(item_id: int, db: Session = Depends(get_db),):
    db_item = item_service.get_item_by_id(db, item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item


@router.post("/")
def create_item(item_create: item_dto.ItemCreate, db: Session = Depends(get_db)):

    result = item_service.create_item(db=db, item_create=item_create)

    if not result:
        return {"result": "Rubro already exist"}
    else:
        return {"result": "success"}


@router.post("/update/{item_id}")
def update_item(item_id: int, item_update: item_dto.ItemUpdate, db: Session = Depends(get_db)):

    db_item = item_service.update_item(db, item_id, item_update)

    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    return db_item


@router.post("/delete/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):

    try:

        result = item_service.delete_item(db, item_id)

        if not result:
            return {"result": "some job use this area"}
        else:
            return {"result": "success"}

    except Exception as e:
        print(e)
        return {"result": "error", "detail": "Error on delete item phone"}
