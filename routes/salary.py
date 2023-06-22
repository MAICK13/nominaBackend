from fastapi import APIRouter, Depends, HTTPException, status

from services import salary_service

from models import salary_dto

from sqlalchemy.orm import Session
from database.database import SessionLocal


router = APIRouter(
    prefix="/salary",
    tags=["Salary"],
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
def get_salary(skip: int = 0, limit: int = 1000, db: Session = Depends(get_db)):
    salaries = salary_service.get_salaries(db, skip=skip, limit=limit)
    return salaries


@router.get("/{salary_id}")
def get_salary_by_id(salary_id: int, db: Session = Depends(get_db),):
    db_salary = salary_service.get_salary_by_id(db, salary_id)
    if db_salary is None:
        raise HTTPException(status_code=404, detail="Salary not found")
    return db_salary


@router.post("/")
def create_salary(salary: salary_dto.SalaryCreate, db: Session = Depends(get_db)):

    result = salary_service.create_salary(db=db, salary_create=salary)

    if not result:
        return {"result": "Salary already exist"}
    else:
        return {"result": "success"}


@router.post("/update/{salary_id}")
def update_salary(salary_id: int, salary_update: salary_dto.SalaryUpdate, db: Session = Depends(get_db)):

    db_salary = salary_service.update_salary(db, salary_id, salary_update)

    if db_salary is None:
        raise HTTPException(status_code=404, detail="Salary not found")

    return db_salary


@router.post("/delete/{salary_id}")
def delete_salary(salary_id: int, db: Session = Depends(get_db)):

    try:

        result = salary_service.delete_salary(db, salary_id)

        if not result:
            return {"result": "some job use this area"}
        else:
            return {"result": "success"}

    except Exception as e:
        print(e)
        return {"result": "error", "detail": "Error on delete salary phone"}
