from fastapi import APIRouter, Depends, HTTPException, status

from services import salary_detail_service

from models import salary_detail_dto

from sqlalchemy.orm import Session
from database.database import SessionLocal


router = APIRouter(
    prefix="/salary_detail",
    tags=["Salary Detail"],
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
def get_salary_detail(skip: int = 0, limit: int = 1000, db: Session = Depends(get_db)):
    salary = salary_detail_service.get_salary_detail(db, skip=skip, limit=limit)
    return salary


@router.get("/{salary_detail_id}")
def get_salary_detail_by_id(salary_detail_id: int, db: Session = Depends(get_db),):
    db_salary = salary_detail_service.get_salary_detail_by_id(db, salary_detail_id)
    if db_salary is None:
        raise HTTPException(status_code=404, detail="Salary detail not found")
    return db_salary


@router.post("/")
def create_salary_detail(salary_detail_create: salary_detail_dto.SalaryDetailCreate, db: Session = Depends(get_db)):

    result = salary_detail_service.create_salary_detail(db=db, salary_detail_create=salary_detail_create)

    if not result:
        return {"result": "Salary detail already exist"}
    else:
        return {"result": "success"}


@router.post("/update/{salary_detail_id}")
def update_salary_detail(salary_detail_id: int, salary_detail_update: salary_detail_dto.SalaryDetailUpdate,
                         db: Session = Depends(get_db)):

    db_salary = salary_detail_service.update_salary_detail(db, salary_detail_id, salary_detail_update)

    if db_salary is None:
        raise HTTPException(status_code=404, detail="Salary detail not found")

    return db_salary


@router.post("/delete/{salary_detail_id}")
def delete_salary_detail(salary_detail_id: int, db: Session = Depends(get_db)):

    try:

        result = salary_detail_service.delete_salary_detail(db, salary_detail_id)

        if not result:
            return {"result": "some job use this area"}
        else:
            return {"result": "success"}

    except Exception as e:
        print(e)
        return {"result": "error", "detail": "Error on delete salary detail item phone"}
