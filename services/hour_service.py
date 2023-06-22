from sqlalchemy.orm import Session

import models.hour_model as hour_model
import models.hour_dto as hour_dto


def get_hours(db: Session, skip: int = 0, limit: int = 1000):
    rows = db.query(hour_model.Hour).filter(hour_model.Hour.hour_status == 1).offset(skip).limit(limit).all()
    results = []
    for hour in rows:
        result = hour_dto.HourResult(
            start_date=str(hour.start_date),
            end_date=str(hour.end_date),
            hour=hour.hour,

            employee_name=hour.employee_info.employee_name + " " +
                          hour.employee_info.employee_last_name,
            key=1
        )
        results.append(result)

    return results


def get_hour_by_id(db, hour_id):
    return db.query(hour_model.Hour).filter(hour_model.Hour.key == hour_id, hour_model.Hour.hour_status == 1).first()


def create_hour(db: Session, hour_create: hour_dto.HourCreate):

    exist_hour = db.query(hour_model.Hour).filter(
        hour_model.Hour.employee == hour_create.employee,
        hour_model.Hour.start_date == hour_create.start_date,
        hour_model.Hour.end_date == hour_create.end_date, hour_model.Hour.hour_status == 1).first()

    if exist_hour is not None:
        return False

    db_hour = hour_model.Hour(start_date=hour_create.start_date, end_date=hour_create.end_date, hour=hour_create.hour,
                              hour_status=1, employee=hour_create.employee)

    db.add(db_hour)
    db.commit()
    db.refresh(db_hour)

    return db_hour


def update_hour(db: Session, hour_id: int, hour_update: hour_dto.HourUpdate):
    db_hour = db.get(hour_model.Hour, hour_id)

    if not db_hour:
        return db_hour

    hour_data = hour_update.dict(exclude_unset=True)

    for key, value in hour_data.items():
        setattr(db_hour, key, value)

    db.add(db_hour)
    db.commit()
    db.refresh(db_hour)

    return db_hour


def delete_hour(db, hour_id):

    db_hour = db.get(hour_model.Hour, hour_id)

    setattr(db_hour, 'hour_status', 0)

    db.add(db_hour)
    db.commit()
    db.refresh(db_hour)

    return db_hour
