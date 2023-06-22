from sqlalchemy.orm import Session

import models.salary_detail_model as salary_detail_model
import models.salary_detail_dto as salary_detail_dto


def get_salary_detail(db: Session, skip: int = 0, limit: int = 1000):
    return db.query(salary_detail_model.SalaryDetail).filter(salary_detail_model.SalaryDetail.salary_status == 1)\
        .offset(skip).limit(limit).all()


def get_salary_detail_by_id(db, salary_detail_id):
    return db.query(salary_detail_model.SalaryDetail).filter(salary_detail_model.SalaryDetail.key == salary_detail_id,
                                                             salary_detail_model.SalaryDetail.salary_status == 1)\
        .first()


def create_salary_detail(db: Session, salary_detail_create: salary_detail_dto.SalaryDetailCreate):

    exist_salary = db.query(salary_detail_model.SalaryDetail).filter(
        salary_detail_model.SalaryDetail.salary == salary_detail_create.salary,
        salary_detail_model.SalaryDetail.salary_item == salary_detail_create.salary_item,
        salary_detail_model.SalaryDetail.salary_status == 1).first()

    if exist_salary is not None:
        return False

    db_salary = salary_detail_model.SalaryDetail(salary_correlative=salary_detail_create.salary_correlative,
                                                 salary_item=salary_detail_create.salary_item,
                                                 salary_mto=salary_detail_create.salary_mto, salary_status=1,
                                                 salary=salary_detail_create.salary)

    db.add(db_salary)
    db.commit()
    db.refresh(db_salary)

    return db_salary


def update_salary_detail(db: Session, salary_detail_id: int,
                         salary_detail_update: salary_detail_dto.SalaryDetailUpdate):

    db_salary = db.get(salary_detail_model.SalaryDetail, salary_detail_id)

    if not db_salary:
        return db_salary

    salary_detail_data = salary_detail_update.dict(exclude_unset=True)

    for key, value in salary_detail_data.items():
        setattr(db_salary, key, value)

    db.add(db_salary)
    db.commit()
    db.refresh(db_salary)

    return db_salary


def delete_salary_detail(db, salary_detail_id):

    db_salary = db.get(salary_detail_model.SalaryDetail, salary_detail_id)

    setattr(db_salary, 'salary_status', 0)

    db.add(db_salary)
    db.commit()
    db.refresh(db_salary)

    return db_salary
