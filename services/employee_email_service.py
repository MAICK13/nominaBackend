from sqlalchemy.orm import Session

import models.employee_email_model as employee_email_model
import models.employee_email_dto as employee_email_dto


def get_employee_email(db: Session, skip: int = 0, limit: int = 1000):
    rows = db.query(employee_email_model.Email).filter(employee_email_model.Email.email_status == 1)\
        .join(employee_email_model.Email.employee_info).offset(skip).limit(limit).all()

    results = []
    for employee_email_row in rows:
        result = employee_email_dto.EmailResult(
            email_type=employee_email_row.email_type,
            employee_email=employee_email_row.employee_email,
            employee_name=employee_email_row.employee_info.employee_name+ " "
                          +employee_email_row.employee_info.employee_last_name,
            key=employee_email_row.key
        )
        results.append(result)

    return results


def get_employee_email_by_id(db, employee_email_id):
    return db.query(employee_email_model.Email).filter(employee_email_model.Email.key == employee_email_id,
                                                       employee_email_model.Email.email_status == 1).first()


def create_employee_email(db: Session, employee_email_create: employee_email_dto.EmailCreate):

    exist_email = db.query(employee_email_model.Email).filter(
        employee_email_model.Email.employee == employee_email_create.employee,
        employee_email_model.Email.email_status == 1).first()

    if exist_email is not None:
        return False

    db_email = employee_email_model.Email(email_type=employee_email_create.email_type,
                                          employee_email=employee_email_create.employee_email,
                                          email_indicator=employee_email_create.email_indicator,
                                          email_status=1, employee=employee_email_create.employee)

    db.add(db_email)
    db.commit()
    db.refresh(db_email)

    return db_email


def update_employee_email(db: Session, employee_email_id: int,
                          employee_email_update: employee_email_dto.EmailUpdate):
    db_email = db.get(employee_email_model.Email, employee_email_id)

    if not db_email:
        return db_email

    employee_phone_data = employee_email_update.dict(exclude_unset=True)

    for key, value in employee_phone_data.items():
        setattr(db_email, key, value)

    db.add(db_email)
    db.commit()
    db.refresh(db_email)

    return db_email


def delete_employee_email(db, employee_email_id):

    db_email = db.get(employee_email_model.Email, employee_email_id)

    setattr(db_email, 'email_status', 0)

    db.add(db_email)
    db.commit()
    db.refresh(db_email)

    return db_email
