from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database.database import Base


class Address(Base):
    __tablename__ = "NOM_DIRECCION_EMPLEADO"

    key = Column("DIR_IdDireccion", Integer, primary_key=True, index=True)
    address_type = Column("DIR_TipoDireccion", String)
    employee_address = Column("DIR_DireccionEmpleado", String)
    address_indicator = Column("DIR_Indicador", String)
    address_status = Column("DIR_EstadoDireccion", Integer)

    employee = Column("FIC_IdEmpleado", Integer, ForeignKey("NOM_FICHA_EMPLEADO.FIC_IdEmpleado"))

    employee_info = relationship("Employee", back_populates="employee_address")
