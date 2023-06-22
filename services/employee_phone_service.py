from sqlalchemy.orm import Session

import models.employee_phone_model as employee_phone_model
import models.employee_phone_dto as employee_phone_dto


def get_employee_phone(db: Session, skip: int = 0, limit: int = 1000):
    rows = db.query(employee_phone_model.EmployeePhone).filter(employee_phone_model.EmployeePhone.phone_status == 1)\
        .join(employee_phone_model.EmployeePhone.employee_info).offset(skip).limit(limit).all()

    results = []
    for employee_phone in rows:
        result = employee_phone_dto.EmployeePhoneResult(
            phone_type=employee_phone.phone_type,
            phone_number=employee_phone.phone_number,
            employee_name=employee_phone.employee_info.employee_name + " " +
                          employee_phone.employee_info.employee_last_name,
            key=employee_phone.key,
            phone_indicator=employee_phone.phone_indicator
        )
        results.append(result)

    return results


def get_employee_phone_by_id(db, employee_phone_id):
    return db.query(employee_phone_model.EmployeePhone).filter(employee_phone_model.EmployeePhone.key
                                                               == employee_phone_id,
                                                               employee_phone_model.EmployeePhone.phone_status == 1)\
        .first()


def create_employee_phone(db: Session, employee_phone_create: employee_phone_dto.EmployeePhoneCreate):

    exist_phone = db.query(employee_phone_model.EmployeePhone).filter(employee_phone_model.EmployeePhone.phone_number
                                                                      == employee_phone_create.phone_number,
                                                                      employee_phone_model.EmployeePhone.phone_status
                                                                      == 1).first()

    if exist_phone is not None:
        return False

    db_employee_phone = employee_phone_model.EmployeePhone(phone_type=employee_phone_create.phone_type,
                                                           phone_number=employee_phone_create.phone_number,
                                                           phone_indicator=employee_phone_create.phone_indicator,
                                                           phone_status=1, employee=employee_phone_create.employee)

    db.add(db_employee_phone)
    db.commit()
    db.refresh(db_employee_phone)

    return db_employee_phone


def update_employee_phone(db: Session, employee_phone_id: int,
                          employee_phone_update: employee_phone_dto.EmployeePhoneUpdate):
    db_employee_phone = db.get(employee_phone_model.EmployeePhone, employee_phone_id)

    if not db_employee_phone:
        return db_employee_phone

    employee_phone_data = employee_phone_update.dict(exclude_unset=True)

    for key, value in employee_phone_data.items():
        setattr(db_employee_phone, key, value)

    db.add(db_employee_phone)
    db.commit()
    db.refresh(db_employee_phone)

    return db_employee_phone


def delete_employee_phone(db, employee_phone_id):

    db_employee_phone = db.get(employee_phone_model.EmployeePhone, employee_phone_id)

    setattr(db_employee_phone, 'phone_status', 0)

    db.add(db_employee_phone)
    db.commit()
    db.refresh(db_employee_phone)

    return db_employee_phone
