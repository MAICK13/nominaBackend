from fastapi import APIRouter, Depends, HTTPException, status

from sqlalchemy.orm import Session
from database.database import SessionLocal

from services import job_service
from models import job_dto

router = APIRouter(
    prefix="/job",
    tags=["Job"],
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
def get_jobs(skip: int = 0, limit: int = 1000, db: Session = Depends(get_db)):
    jobs = job_service.get_jobs(db, skip=skip, limit=limit)
    return jobs


@router.get("/{job_id}")
def get_job_by_id(job_id: int, db: Session = Depends(get_db),):
    db_job = job_service.get_job(db, job_id)
    if db_job is None:
        raise HTTPException(status_code=404, detail="Job not found")
    return db_job


@router.post("/")
def create_job(job: job_dto.JobCreate, db: Session = Depends(get_db)):

    result = job_service.create_job(db=db, job_create=job)

    if not result:
        return {"result": "job already exist"}
    else:
        return {"result": "success"}


@router.post("/update/{job_id}")
def update_job(job_id: int, job: job_dto.JobUpdate, db: Session = Depends(get_db)):

    db_job = job_service.update_job(db, job_id, job)

    if db_job is None:
        raise HTTPException(status_code=404, detail="Job not found")

    return db_job


@router.post("/delete/{job_id}")
def delete_area(job_id: int, db: Session = Depends(get_db)):

    try:

        result = job_service.delete_job(db, job_id)

        if not result:
            return {"result": "some employee use this area"}
        else:
            return {"result": "success"}

    except Exception as e:
        print(e)
        return {"result": "error", "detail": "Error on delete job"}

