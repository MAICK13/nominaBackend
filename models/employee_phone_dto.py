from pydantic import BaseModel


class EmployeePhoneBase(BaseModel):
    phone_type: str
    phone_number: int
    phone_indicator: str
    phone_status: int
    employee: int


class EmployeePhoneResult(BaseModel):
    key: int
    phone_type: str
    phone_number: int
    employee_name: str
    phone_indicator: str


class EmployeePhoneCreate(BaseModel):
    phone_type: str
    phone_number: int
    phone_indicator: str
    employee: int


class EmployeePhoneUpdate(BaseModel):
    phone_type: str
    phone_number: int
    phone_indicator: str
    employee: int


class EmployeePhone(EmployeePhoneBase):
    employee_phone_id: int

    class Config:
        orm_mode = True

