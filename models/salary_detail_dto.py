from pydantic import BaseModel


class SalaryDetailBase(BaseModel):
    salary_correlative: int
    salary_item: int
    salary_mto: float
    salary_status: int
    salary: int


class SalaryDetailCreate(BaseModel):
    salary_correlative: int
    salary_item: int
    salary_mto: float
    salary: int


class SalaryDetailUpdate(BaseModel):
    salary_correlative: int
    salary_item: int
    salary_mto: float
    salary: int


class SalaryDetail(SalaryDetailBase):
    salary_detail_id: int

    class Config:
        orm_mode = True

