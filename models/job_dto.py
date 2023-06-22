from pydantic import BaseModel


class JobBase(BaseModel):
    job_name: str
    job_description: str
    job_state: int
    job_salary: float
    area: int


class JobResult(BaseModel):
    job_name: str
    job_description: str
    job_salary: float
    area_name: str
    key: int


class JobCreate(BaseModel):
    job_name: str
    job_description: str
    job_salary: float
    area: int


class JobUpdate(BaseModel):
    job_name: str
    job_description: str
    job_salary: float
    area: int


class Job(JobBase):
    job_id: int

    class Config:
        orm_mode = True

