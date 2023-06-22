from fastapi import APIRouter, Depends, HTTPException, status

from services import vacation_service

from models import vacation_dto

from sqlalchemy.orm import Session
from database.database import SessionLocal


router = APIRouter(
    prefix="/vacation",
    tags=["Vacation"],
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
def get_vacations(skip: int = 0, limit: int = 1000, db: Session = Depends(get_db)):
    vacations = vacation_service.get_vacations(db, skip=skip, limit=limit)
    return vacations


@router.get("/{vacation_id}")
def get_vacation_by_id(vacation_id: int, db: Session = Depends(get_db),):
    db_vacation = vacation_service.get_vacation_by_id(db, vacation_id)
    if db_vacation is None:
        raise HTTPException(status_code=404, detail="Vacation not found")
    return db_vacation


@router.post("/")
def create_vacation(vacation_create: vacation_dto.VacationCreate, db: Session = Depends(get_db)):

    result = vacation_service.create_vacation(db=db, vacation_create=vacation_create)

    if not result:
        return {"result": "Vacation already exist"}
    else:
        return {"result": "success"}


@router.post("/update/{vacation_id}")
def update_vacation(vacation_id: int, vacation_update: vacation_dto.VacationUpdate, db: Session = Depends(get_db)):

    db_salary = vacation_service.update_vacation(db, vacation_id, vacation_update)

    if db_salary is None:
        raise HTTPException(status_code=404, detail="Vacation not found")

    return db_salary


@router.post("/delete/{vacation_id}")
def delete_vacation(vacation_id: int, db: Session = Depends(get_db)):

    try:

        result = vacation_service.delete_vacation(db, vacation_id)

        if not result:
            return {"result": "some job use this area"}
        else:
            return {"result": "success"}

    except Exception as e:
        print(e)
        return {"result": "error", "detail": "Error on delete vacation phone"}
