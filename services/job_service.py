from sqlalchemy.orm import Session
from datetime import datetime

import models.job_model as job_model
import models.job_dto as job_dto


def get_jobs(db: Session, skip: int = 0, limit: int = 1000):
    rows = db.query(job_model.Job).filter(job_model.Job.job_status == 1).offset(skip).limit(limit).all()

    results = []
    for job in rows:
        result = job_dto.JobResult(
            job_name=job.job_name,
            job_description=job.job_description,
            job_salary=job.job_salary,
            area_name=job.area_info.area_name,
            key=job.key
        )
        results.append(result)

    return results


def get_job(db, job_id):
    return db.query(job_model.Job).filter(job_model.Job.key == job_id, job_model.Job.job_status == 1).first()


def create_job(db: Session, job_create: job_dto.JobCreate):

    exist_job = db.query(job_model.Job).filter(job_model.Job.job_name == job_create.job_name,
                                               job_model.Job.job_status == 1).first()

    if exist_job is not None:
        return False

    db_job = job_model.Job(job_name=job_create.job_name, job_description=job_create.job_description, job_status=1,
                           job_salary=job_create.job_salary, area=job_create.area)

    db.add(db_job)
    db.commit()
    db.refresh(db_job)

    return db_job


def update_job(db: Session, job_id: int, job_update: job_dto.JobUpdate):
    db_job = db.get(job_model.Job, job_id)

    if not db_job:
        return db_job

    job_data = job_update.dict(exclude_unset=True)

    for key, value in job_data.items():
        setattr(db_job, key, value)

    db.add(db_job)
    db.commit()
    db.refresh(db_job)

    return db_job


def delete_job(db, job_id):

    db_job = db.get(job_model.Job, job_id)

    setattr(db_job, 'job_status', 0)

    db.add(db_job)
    db.commit()
    db.refresh(db_job)

    return db_job
