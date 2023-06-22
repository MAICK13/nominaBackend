from pydantic import BaseModel


class AddressBase(BaseModel):
    address_type: str
    employee_address: str
    address_indicator: str
    address_status: int
    employee: int


class AddressResult(BaseModel):
    address_type: str
    employee_address: str
    employee_name: str
    key: int


class AddressCreate(BaseModel):
    address_type: str
    employee_address: str
    address_indicator: str
    employee: int


class AddressUpdate(BaseModel):
    address_type: str
    employee_address: str
    address_indicator: str
    employee: int


class Address(AddressBase):
    item_id: int

    class Config:
        orm_mode = True

