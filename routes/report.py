from fastapi import APIRouter, Depends, HTTPException, status
import base64
from fastapi.responses import FileResponse

from services import report_service

from models import report_dto

from sqlalchemy.orm import Session
from database.database import SessionLocal


router = APIRouter(
    prefix="/report",
    tags=["Reports"],
    responses={404: {"description": "Not found"}},
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/area")
def get_areas_report(db: Session = Depends(get_db)):

    report_name = report_service.get_areas_report(db)

    with open(report_name, "rb") as file:
        file_content = file.read()

    file_result = base64.b64encode(file_content)

    return {"archivo_base64": file_result}


@router.get("/job")
def get_job_report(db: Session = Depends(get_db)):

    report_name = report_service.get_job_report(db)

    with open(report_name, "rb") as file:
        file_content = file.read()

    file_result = base64.b64encode(file_content)

    return {"archivo_base64": file_result}


@router.get("/employee_phone")
def get_employee_phone(db: Session = Depends(get_db)):

    report_name = report_service.get_employee_phone(db)

    with open(report_name, "rb") as file:
        file_content = file.read()

    file_result = base64.b64encode(file_content)

    return {"archivo_base64": file_result}


@router.get("/employee_email")
def get_employee_email(db: Session = Depends(get_db)):

    report_name = report_service.get_employee_email(db)

    with open(report_name, "rb") as file:
        file_content = file.read()

    file_result = base64.b64encode(file_content)

    return {"archivo_base64": file_result}


@router.get("/employee_address")
def get_employee_address(db: Session = Depends(get_db)):

    report_name = report_service.get_employee_address(db)

    with open(report_name, "rb") as file:
        file_content = file.read()

    file_result = base64.b64encode(file_content)

    return {"archivo_base64": file_result}


@router.get("/employee_item")
def get_employee_item(db: Session = Depends(get_db)):

    report_name = report_service.get_employee_item(db)

    with open(report_name, "rb") as file:
        file_content = file.read()

    file_result = base64.b64encode(file_content)

    return {"archivo_base64": file_result}


@router.get("/item")
def get_item(db: Session = Depends(get_db)):

    report_name = report_service.get_item(db)

    with open(report_name, "rb") as file:
        file_content = file.read()

    file_result = base64.b64encode(file_content)

    return {"archivo_base64": file_result}


@router.get("/vacation")
def get_vacations(db: Session = Depends(get_db)):

    report_name = report_service.get_vacation(db)

    with open(report_name, "rb") as file:
        file_content = file.read()

    file_result = base64.b64encode(file_content)

    return {"archivo_base64": file_result}


@router.get("/employee")
def get_employees(db: Session = Depends(get_db)):

    report_name = report_service.get_employees(db)

    with open(report_name, "rb") as file:
        file_content = file.read()

    file_result = base64.b64encode(file_content)

    return {"archivo_base64": file_result}


@router.get("/hours")
def get_hours(db: Session = Depends(get_db)):

    report_name = report_service.get_hours(db)

    with open(report_name, "rb") as file:
        file_content = file.read()

    file_result = base64.b64encode(file_content)

    return {"archivo_base64": file_result}


@router.post("/payroll")
def generate_payroll(payroll_data: report_dto.PayrollCreate, db: Session = Depends(get_db)):

    report_name = report_service.get_payroll(payroll_data, db)

    with open(report_name, "rb") as file:
        file_content = file.read()

    file_result = base64.b64encode(file_content)

    return {"archivo_base64": file_result}


@router.post("/ticket")
def generate_payroll(ticket_data: report_dto.TicketCreate, db: Session = Depends(get_db)):

    report_name = report_service.get_ticket(ticket_data, db)

    with open(report_name, "rb") as file:
        file_content = file.read()

    file_result = base64.b64encode(file_content)

    return {"archivo_base64": file_result}



