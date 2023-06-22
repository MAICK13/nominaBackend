from sqlalchemy.orm import Session

import models.vacation_model as vacation_model
import models.vacation_dto as vacation_dto


def get_vacations(db: Session, skip: int = 0, limit: int = 1000):
    return db.query(vacation_model.Vacation).filter(vacation_model.Vacation.vacation_status == 1)\
        .join(vacation_model.Vacation.employee_info).offset(skip).limit(limit).all()

    # results = []
    # for vacation_row in rows:
    #     result = vacation_dto.VacationResult(
    #         request_date=vacation_row.request_date,
    #         # start_date=vacation_row.start_date,
    #         # end_date=vacation_row.end_date,
    #         # left_days=vacation_row.left_days,
    #         # date_approval=vacation_row.date_approval,
    #         # date_rejection=vacation_row.date_rejection,
    #         # rejection_reason=vacation_row.rejection_reason,
    #         # key=vacation_row.key,
    #         employee_name=vacation_row.employee_info.employee_name+ " "
    #                       +vacation_row.employee_info.employee_last_name,
    #     )
    #     results.append(result)
    #
    # return results


def get_vacation_by_id(db, vacation_id):
    return db.query(vacation_model.Vacation).filter(vacation_model.Vacation.key == vacation_id,
                                                    vacation_model.Vacation.vacation_status == 1).first()


def create_vacation(db: Session, vacation_create: vacation_dto.VacationCreate):

    exist_vacation = db.query(vacation_model.Vacation).filter(
        vacation_model.Vacation.start_date == vacation_create.start_date,
        vacation_model.Vacation.end_date == vacation_create.end_date,
        vacation_model.Vacation.employee == vacation_create.employee,
        vacation_model.Vacation.vacation_status == 1).first()

    if exist_vacation is not None:
        return False

    db_vacation = vacation_model.Vacation(request_date=vacation_create.request_date,
                                          start_date=vacation_create.start_date,
                                          end_date=vacation_create.end_date,
                                          left_days=vacation_create.left_days, vacation_status=1,
                                          date_approval=vacation_create.date_approval,
                                          date_rejection=vacation_create.date_rejection,
                                          rejection_reason=vacation_create.rejection_reason,
                                          employee=vacation_create.employee)

    db.add(db_vacation)
    db.commit()
    db.refresh(db_vacation)

    return db_vacation


def update_vacation(db: Session, vacation_id: int, vacation_update: vacation_dto.VacationUpdate):
    db_vacation = db.get(vacation_model.Vacation, vacation_id)

    if not db_vacation:
        return db_vacation

    employee_phone_data = vacation_update.dict(exclude_unset=True)

    for key, value in employee_phone_data.items():
        setattr(db_vacation, key, value)

    db.add(db_vacation)
    db.commit()
    db.refresh(db_vacation)

    return db_vacation


def delete_vacation(db, vacation_id):

    db_vacation = db.get(vacation_model.Vacation, vacation_id)

    setattr(db_vacation, 'vacation_status', 0)

    db.add(db_vacation)
    db.commit()
    db.refresh(db_vacation)

    return db_vacation
