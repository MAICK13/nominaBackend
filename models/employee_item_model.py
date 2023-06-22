from sqlalchemy import Column, Integer, ForeignKey, Float, String
from sqlalchemy.orm import relationship

from database.database import Base


class EmployeeItem(Base):
    __tablename__ = "NOM_RUBRO_EMPLEADO"

    key = Column("RUE_IdRubroEmpleado", Integer, primary_key=True, index=True)
    item_status = Column("RUE_Estado", Integer)
    employee = Column("FIC_IdEmpleado", Integer, ForeignKey("NOM_FICHA_EMPLEADO.FIC_IdEmpleado"))
    item = Column("RUB_IdRubro", Integer, ForeignKey("NOM_RUBRO.RUB_IdRubro"))
    item_mont = Column("RUE_Monto", Float)
    item_fact = Column("RUE_Factor", String)

    employee_info = relationship("Employee", back_populates="employee_item")
    item_info = relationship("Item", back_populates="employee_item")
