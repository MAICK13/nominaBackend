from pydantic import BaseModel


class SalaryBase(BaseModel):
    pay_date: str
    salary_status: int
    employee: int


class SalaryCreate(BaseModel):
    pay_date: str
    employee: int


class SalaryUpdate(BaseModel):
    pay_date: str
    employee: int


class Salary(SalaryBase):
    salary_id: int

    class Config:
        orm_mode = True

