from pydantic import BaseModel


class EmailBase(BaseModel):
    email_type: str
    employee_email: str
    email_indicator: str
    email_status: int
    employee: int


class EmailResult(BaseModel):
    email_type: str
    employee_email: str
    employee_name: str
    key: int


class EmailCreate(BaseModel):
    email_type: str
    employee_email: str
    email_indicator: str
    employee: int


class EmailUpdate(BaseModel):
    email_type: str
    employee_email: str
    email_indicator: str
    employee: int


class Email(EmailBase):
    email_id: int

    class Config:
        orm_mode = True

