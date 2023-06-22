from pydantic import BaseModel


class EmployeeBase(BaseModel):
    employee_name: str
    employee_second_name: str
    employee_other_name: str
    employee_last_name: str
    employee_second_last_name: str
    employee_last_name_married: str
    employee_dpi: str
    employee_born_date: str
    employee_born_place: str
    employee_gender: str
    employee_civil_state: str
    employee_start_date: str
    employee_contract: str
    employee_status: int
    job: int


class EmployeeResult(BaseModel):
    employee_name: str
    employee_second_name: str
    employee_other_name: str
    employee_last_name: str
    employee_second_last_name: str
    employee_last_name_married: str
    employee_dpi: str
    employee_born_date: str
    employee_born_place: str
    employee_gender: str
    employee_civil_state: str
    employee_start_date: str
    employee_contract: str
    job_name: str
    key: int


class EmployeeCreate(BaseModel):
    employee_name: str
    employee_second_name: str
    employee_other_name: str
    employee_last_name: str
    employee_second_last_name: str
    employee_last_name_married: str
    employee_dpi: str
    employee_born_date: str
    employee_born_place: str
    employee_gender: str
    employee_civil_state: str
    employee_start_date: str
    employee_contract: str
    job: int


class EmployeeUpdate(BaseModel):
    employee_name: str
    employee_second_name: str
    employee_other_name: str
    employee_last_name: str
    employee_second_last_name: str
    employee_last_name_married: str
    employee_dpi: str
    employee_born_date: str
    employee_born_place: str
    employee_gender: str
    employee_civil_state: str
    employee_start_date: str
    employee_contract: str
    job: int


class Employee(EmployeeBase):
    employee_id: int

    class Config:
        orm_mode = True

