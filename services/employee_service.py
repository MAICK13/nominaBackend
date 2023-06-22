from sqlalchemy.orm import Session

import models.employee_model as employee_model
import models.employee_dto as employee_dto


def get_employees(db: Session, skip: int = 0, limit: int = 1000):
    rows = db.query(employee_model.Employee).filter(employee_model.Employee.employee_status == 1)\
        .offset(skip).limit(limit).all()

    results = []
    for employee in rows:
        result = employee_dto.EmployeeResult(
            employee_name=employee.employee_name,
            employee_second_name=employee.employee_second_name,
            employee_other_name=employee.employee_other_name,
            employee_last_name=employee.employee_last_name,
            employee_second_last_name=employee.employee_second_last_name,
            employee_last_name_married=employee.employee_last_name_married,
            employee_dpi=employee.employee_dpi,
            employee_born_date=str(employee.employee_born_date),
            employee_born_place=employee.employee_born_place,
            employee_gender=employee.employee_gender,
            employee_civil_state=employee.employee_civil_state,
            employee_start_date=str(employee.employee_start_date),
            employee_contract=employee.employee_contract,
            job_name=employee.employee_job.job_name,
            key=employee.key
        )
        results.append(result)

    return results


def get_employee(db, employee_id):
    return db.query(employee_model.Employee).filter(employee_model.Employee.key == employee_id,
                                                    employee_model.Employee.employee_status == 1).first()


def create_employee(db: Session, employee_create: employee_dto.EmployeeCreate):

    exist_area = db.query(employee_model.Employee).filter(employee_model.Employee.employee_name ==
                                                          employee_create.employee_name,
                                                          employee_model.Employee.employee_last_name ==
                                                          employee_create.employee_last_name,
                                                          employee_model.Employee.employee_status == 1).first()

    if exist_area is not None:
        return False

    db_employee = employee_model.Employee(employee_name=employee_create.employee_name,
                                          employee_second_name=employee_create.employee_second_name,
                                          employee_other_name=employee_create.employee_other_name,
                                          employee_last_name=employee_create.employee_last_name,
                                          employee_second_last_name=employee_create.employee_second_last_name,
                                          employee_last_name_married=employee_create.employee_last_name_married,
                                          employee_dpi=employee_create.employee_dpi,
                                          employee_born_date=employee_create.employee_born_date,
                                          employee_born_place=employee_create.employee_born_place,
                                          employee_gender=employee_create.employee_gender,
                                          employee_civil_state=employee_create.employee_civil_state,
                                          employee_start_date=employee_create.employee_start_date,
                                          employee_contract=employee_create.employee_contract, employee_status=1,
                                          job=employee_create.job)

    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)

    return db_employee


def update_employee(db: Session, employee_id: int, employee_update: employee_dto.EmployeeUpdate):
    db_employee = db.get(employee_model.Employee, employee_id)

    if not db_employee:
        return db_employee

    employee_data = employee_update.dict(exclude_unset=True)

    for key, value in employee_data.items():
        setattr(db_employee, key, value)

    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)

    return db_employee


def delete_employee(db, employee_id):

    db_employee = db.get(employee_model.Employee, employee_id)

    setattr(db_employee, 'employee_status', 0)

    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)

    return db_employee
