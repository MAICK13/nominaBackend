from fastapi import APIRouter, Depends, HTTPException, status

from services import employee_service

from models import employee_dto

from sqlalchemy.orm import Session
from database.database import SessionLocal


router = APIRouter(
    prefix="/employee",
    tags=["Employee"],
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
def get_employees(skip: int = 0, limit: int = 1000, db: Session = Depends(get_db)):
    employees = employee_service.get_employees(db, skip=skip, limit=limit)
    return employees


@router.get("/{employee_id}")
def get_employee_by_id(employee_id: int, db: Session = Depends(get_db),):
    db_area = employee_service.get_employee(db, employee_id)
    if db_area is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_area


@router.post("/")
def create_employee(employee: employee_dto.EmployeeCreate, db: Session = Depends(get_db)):

    result = employee_service.create_employee(db=db, employee_create=employee)

    if not result:
        return {"result": "Employee already exist"}
    else:
        return {"result": "success"}


@router.post("/update/{employee_id}")
def update_employee(employee_id: int, employee: employee_dto.EmployeeUpdate, db: Session = Depends(get_db)):

    db_employee = employee_service.update_employee(db, employee_id, employee)

    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")

    return db_employee


@router.post("/delete/{employee_id}")
def delete_employee(employee_id: int, db: Session = Depends(get_db)):

    try:

        result = employee_service.delete_employee(db, employee_id)

        if not result:
            return {"result": "some job use this area"}
        else:
            return {"result": "success"}

    except Exception as e:
        print(e)
        return {"result": "error", "detail": "Error on delete employee"}
