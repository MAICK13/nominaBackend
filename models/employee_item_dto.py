from pydantic import BaseModel


class EmployeeItemBse(BaseModel):
    item_status: int
    employee: int
    item: int


class EmployeeItemResult(BaseModel):
    employee_name: str
    item: str
    item_mont: float
    item_fact: str
    key: int


class EmployeeItemCreate(BaseModel):
    employee: int
    item: int
    item_mont: float
    item_fact: str


class EmployeeItemUpdate(BaseModel):
    employee: int
    item: int
    item_mont: float
    item_fact: str


class EmployeeItem(EmployeeItemBse):
    employee_item_id: int

    class Config:
        orm_mode = True

