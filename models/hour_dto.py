from pydantic import BaseModel


class HourBse(BaseModel):
    start_date: str
    end_date: str
    hour: int
    hour_status: int
    employee: int


class HourResult(BaseModel):
    start_date: str
    end_date: str
    hour: int
    employee_name: str
    key: int


class HourCreate(BaseModel):
    start_date: str
    end_date: str
    hour: int
    employee: int


class HourUpdate(BaseModel):
    start_date: str
    end_date: str
    hour: int
    employee: int


class Hour(HourBse):
    hour_id: int

    class Config:
        orm_mode = True

