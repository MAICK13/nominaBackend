from fastapi import APIRouter, Depends, HTTPException, status

from services import employee_item_service

from models import employee_item_dto

from sqlalchemy.orm import Session
from database.database import SessionLocal


router = APIRouter(
    prefix="/employee_item",
    tags=["Employee Item"],
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
def get_employee_item(skip: int = 0, limit: int = 1000, db: Session = Depends(get_db)):
    items = employee_item_service.get_employee_item(db, skip=skip, limit=limit)
    return items


@router.get("/{employee_item_id}")
def get_employee_item_by_id(employee_item_id: int, db: Session = Depends(get_db),):
    db_item = employee_item_service.get_employee_item_by_id(db, employee_item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Employee Item not found")
    return db_item


@router.post("/")
def create_employee_item(employee_item_create: employee_item_dto.EmployeeItemCreate, db: Session = Depends(get_db)):

    result = employee_item_service.create_employee_item(db=db, employee_item_create=employee_item_create)

    if not result:
        return {"result": "Employee item already exist"}
    else:
        return {"result": "success"}


@router.post("/update/{employee_item_id}")
def update_employee_item(employee_item_id: int, employee_item_update: employee_item_dto.EmployeeItemUpdate,
                         db: Session = Depends(get_db)):

    db_item = employee_item_service.update_employee_item(db, employee_item_id, employee_item_update)

    if db_item is None:
        raise HTTPException(status_code=404, detail="Employee item not found")

    return db_item


@router.post("/delete/{employee_item_id}")
def delete_employee_item(employee_item_id: int, db: Session = Depends(get_db)):

    try:

        result = employee_item_service.delete_employee_item(db, employee_item_id)

        if not result:
            return {"result": "some job use this area"}
        else:
            return {"result": "success"}

    except Exception as e:
        print(e)
        return {"result": "error", "detail": "Error on delete employee item phone"}
