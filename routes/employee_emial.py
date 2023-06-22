from fastapi import APIRouter, Depends, HTTPException, status

from services import employee_email_service

from models import employee_email_dto

from sqlalchemy.orm import Session
from database.database import SessionLocal


router = APIRouter(
    prefix="/employee_email",
    tags=["Employee Email"],
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
def get_employee_email(skip: int = 0, limit: int = 1000, db: Session = Depends(get_db)):
    emails = employee_email_service.get_employee_email(db, skip=skip, limit=limit)
    return emails


@router.get("/{employee_email_id}")
def get_employee_email_by_id(employee_email_id: int, db: Session = Depends(get_db),):
    db_email = employee_email_service.get_employee_email_by_id(db, employee_email_id)
    if db_email is None:
        raise HTTPException(status_code=404, detail="Employee Email not found")
    return db_email


@router.post("/")
def create_employee_email(employee_email_create: employee_email_dto.EmailCreate, db: Session = Depends(get_db)):

    result = employee_email_service.create_employee_email(db=db, employee_email_create=employee_email_create)

    if not result:
        return {"result": "Employee Email already exist"}
    else:
        return {"result": "success"}


@router.post("/update/{employee_email_id}")
def update_employee_email(employee_email_id: int,
                          employee_email_update: employee_email_dto.EmailUpdate, db: Session = Depends(get_db)):

    db_email = employee_email_service.update_employee_email(db, employee_email_id, employee_email_update)

    if db_email is None:
        raise HTTPException(status_code=404, detail="Employee Email not found")

    return db_email


@router.post("/delete/{employee_email_id}")
def delete_employee_email(employee_email_id: int, db: Session = Depends(get_db)):

    try:

        result = employee_email_service.delete_employee_email(db, employee_email_id)

        if not result:
            return {"result": "some job use this area"}
        else:
            return {"result": "success"}

    except Exception as e:
        print(e)
        return {"result": "error", "detail": "Error on delete employee email phone"}
