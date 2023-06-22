from pydantic import BaseModel


class ItemBase(BaseModel):
    item_description: str
    item_sign: str
    item_percentage: int
    item_amount: float
    item_status: int


class ItemCreate(BaseModel):
    item_description: str
    item_type: str


class ItemUpdate(BaseModel):
    item_description: str
    item_type: str


class Item(ItemBase):
    item_id: int

    class Config:
        orm_mode = True

