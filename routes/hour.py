from fastapi import APIRouter, Depends, HTTPException, status

from services import hour_service

from models import hour_dto

from sqlalchemy.orm import Session
from database.database import SessionLocal


router = APIRouter(
    prefix="/hour",
    tags=["Hour"],
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
def get_hours(skip: int = 0, limit: int = 1000, db: Session = Depends(get_db)):
    hours = hour_service.get_hours(db, skip=skip, limit=limit)
    return hours


@router.get("/{hour_id}")
def get_hour_by_id(hour_id: int, db: Session = Depends(get_db),):
    db_email = hour_service.get_hour_by_id(db, hour_id)
    if db_email is None:
        raise HTTPException(status_code=404, detail="Hour not found")
    return db_email


@router.post("/")
def create_hour(hour_create: hour_dto.HourCreate, db: Session = Depends(get_db)):

    result = hour_service.create_hour(db=db, hour_create=hour_create)

    if not result:
        return {"result": "Hour already exist"}
    else:
        return {"result": "success"}


@router.post("/update/{hour_id}")
def update_hour(hour_id: int, hour_update: hour_dto.HourUpdate, db: Session = Depends(get_db)):

    db_hour = hour_service.update_hour(db, hour_id, hour_update)

    if db_hour is None:
        raise HTTPException(status_code=404, detail="Hour not found")

    return db_hour


@router.post("/delete/{hour_id}")
def delete_hour(hour_id: int, db: Session = Depends(get_db)):

    try:

        result = hour_service.delete_hour(db, hour_id)

        if not result:
            return {"result": "some job use this area"}
        else:
            return {"result": "success"}

    except Exception as e:
        print(e)
        return {"result": "error", "detail": "Error on delete hour phone"}
