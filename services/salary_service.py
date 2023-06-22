from sqlalchemy.orm import Session

import models.salary_model as salary_model
import models.salary_dto as salary_dto


def get_salaries(db: Session, skip: int = 0, limit: int = 1000):
    return db.query(salary_model.Salary).filter(salary_model.Salary.salary_status == 1).offset(skip).limit(limit).all()


def get_salary_by_id(db, salary_id):
    return db.query(salary_model.Salary).filter(salary_model.Salary.key == salary_id,
                                                salary_model.Salary.salary_status == 1).first()


def create_salary(db: Session, salary_create: salary_dto.SalaryCreate):

    exist_salary = db.query(salary_model.Salary).filter(salary_model.Salary.employee == salary_create.employee,
                                                        salary_model.Salary.pay_date == salary_create.pay_date,
                                                        salary_model.Salary.salary_status == 1).first()

    if exist_salary is not None:
        return False

    db_salary = salary_model.Salary(pay_date=salary_create.pay_date, salary_status=1, employee=salary_create.employee)

    db.add(db_salary)
    db.commit()
    db.refresh(db_salary)

    return db_salary


def update_salary(db: Session, salary_id: int, salary_update: salary_dto.SalaryUpdate):
    db_salary = db.get(salary_model.Salary, salary_id)

    if not db_salary:
        return db_salary

    employee_phone_data = salary_update.dict(exclude_unset=True)

    for key, value in employee_phone_data.items():
        setattr(db_salary, key, value)

    db.add(db_salary)
    db.commit()
    db.refresh(db_salary)

    return db_salary


def delete_salary(db, salary_id):

    db_salary = db.get(salary_model.Salary, salary_id)

    setattr(db_salary, 'salary_status', 0)

    db.add(db_salary)
    db.commit()
    db.refresh(db_salary)

    return db_salary
