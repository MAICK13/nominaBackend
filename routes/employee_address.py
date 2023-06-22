from fastapi import APIRouter, Depends, HTTPException, status

from services import employee_address_service

from models import employee_address_dto

from sqlalchemy.orm import Session
from database.database import SessionLocal


router = APIRouter(
    prefix="/employee_address",
    tags=["Employee Address"],
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
def get_employee_address(skip: int = 0, limit: int = 1000, db: Session = Depends(get_db)):
    items = employee_address_service.get_employee_address(db, skip=skip, limit=limit)
    return items


@router.get("/{employee_address_id}")
def get_employee_address_by_id(employee_address_id: int, db: Session = Depends(get_db),):
    db_address = employee_address_service.get_employee_address_by_id(db, employee_address_id)
    if db_address is None:
        raise HTTPException(status_code=404, detail="Employee Address not found")
    return db_address


@router.post("/")
def create_employee_address(employee_address_create: employee_address_dto.AddressCreate, db: Session = Depends(get_db)):

    result = employee_address_service.create_employee_address(db=db, employee_address_create=employee_address_create)

    if not result:
        return {"result": "Employee Address already exist"}
    else:
        return {"result": "success"}


@router.post("/update/{employee_address_id}")
def update_employee_address(employee_address_id: int,
                            employee_address_update: employee_address_dto.AddressUpdate, db: Session = Depends(get_db)):

    db_address = employee_address_service.update_employee_address(db, employee_address_id, employee_address_update)

    if db_address is None:
        raise HTTPException(status_code=404, detail="Employee Address not found")

    return db_address


@router.post("/delete/{employee_address_id}")
def delete_employee_address(employee_address_id: int, db: Session = Depends(get_db)):

    try:

        result = employee_address_service.delete_employee_address(db, employee_address_id)

        if not result:
            return {"result": "some job use this area"}
        else:
            return {"result": "success"}

    except Exception as e:
        print(e)
        return {"result": "error", "detail": "Error on delete employee address phone"}
