from pydantic import BaseModel


class PayrollCreate(BaseModel):
    start_date: str
    end_date: str
    pay_date: str
    type: str


class PayrollResult(BaseModel):
    name: str
    last_name: str
    start_date: str
    end_date: str
    item: str
    mont: float


class TicketCreate(BaseModel):
    employee: int





