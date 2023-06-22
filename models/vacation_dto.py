from pydantic import BaseModel


class VacationBase(BaseModel):
    request_date: str
    start_date: str
    end_date: str
    left_days: int
    vacation_status: int
    date_approval: str
    date_rejection: str
    rejection_reason: str
    employee: int


class VacationResult(BaseModel):
    request_date: str
    start_date: str
    end_date: str
    left_days: int
    date_approval: str
    date_rejection: str
    rejection_reason: str
    employee_name: str
    key: int


class VacationCreate(BaseModel):
    request_date: str
    start_date: str
    end_date: str
    left_days: int
    date_approval: str
    date_rejection: str
    rejection_reason: str
    employee: int


class VacationUpdate(BaseModel):
    request_date: str
    start_date: str
    end_date: str
    left_days: int
    date_approval: str
    date_rejection: str
    rejection_reason: str
    employee: int


class Vacation(VacationBase):
    vacation_id: int

    class Config:
        orm_mode = True

