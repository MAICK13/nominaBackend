from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from database.database import Base


class Item(Base):
    __tablename__ = "NOM_RUBRO"

    key = Column("RUB_IdRubro", Integer, primary_key=True, index=True)
    item_description = Column("RUB_Descripcion", String)
    item_type = Column("RUB_Tipo", String)
    item_status = Column("RUB_Estado", Integer)

    employee_item = relationship("EmployeeItem", back_populates="item_info")
