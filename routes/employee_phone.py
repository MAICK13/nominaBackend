from fastapi import APIRouter, Depends, HTTPException, status

from services import employee_phone_service

from models import employee_phone_dto

from sqlalchemy.orm import Session
from database.database import SessionLocal


router = APIRouter(
    prefix="/employee_phone",
    tags=["EmployeePhone"],
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
def get_employee_phone(skip: int = 0, limit: int = 1000, db: Session = Depends(get_db)):
    employee_phone = employee_phone_service.get_employee_phone(db, skip=skip, limit=limit)
    return employee_phone


@router.get("/{employee_phone_id}")
def get_employee_phone_by_id(employee_phone_id: int, db: Session = Depends(get_db),):
    db_employee_phone = employee_phone_service.get_employee_phone_by_id(db, employee_phone_id)
    if db_employee_phone is None:
        raise HTTPException(status_code=404, detail="Employee phone not found")
    return db_employee_phone


@router.post("/")
def create_employee_phone(employee_phone: employee_phone_dto.EmployeePhoneCreate, db: Session = Depends(get_db)):

    result = employee_phone_service.create_employee_phone(db=db, employee_phone_create=employee_phone)

    if not result:
        return {"result": "Employee phone already exist"}
    else:
        return {"result": "success"}


@router.post("/update/{employee_phone_id}")
def update_employee_phone(employee_phone_id: int,
                          employee_phone: employee_phone_dto.EmployeePhoneUpdate, db: Session = Depends(get_db)):

    db_employee_phone = employee_phone_service.update_employee_phone(db, employee_phone_id, employee_phone)

    if db_employee_phone is None:
        raise HTTPException(status_code=404, detail="Employee not found")

    return db_employee_phone


@router.post("/delete/{employee_phone_id}")
def delete_employee_phone(employee_phone_id: int, db: Session = Depends(get_db)):

    try:

        result = employee_phone_service.delete_employee_phone(db, employee_phone_id)

        if not result:
            return {"result": "some job use this area"}
        else:
            return {"result": "success"}

    except Exception as e:
        print(e)
        return {"result": "error", "detail": "Error on delete employee phone"}
