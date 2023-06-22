from sqlalchemy import Column, Integer, String, Date, ForeignKey

from database.database import Base
from sqlalchemy.orm import relationship


class EmployeePhone(Base):
    __tablename__ = "NOM_TEL_EMPLEADO"

    key = Column("TEL_IdTelefono", Integer, primary_key=True, index=True)
    phone_type = Column("TEL_TipoNumero", String)
    phone_number = Column("TEL_Numero", Integer)
    phone_indicator = Column("TEL_Indicador", String)
    phone_status = Column("TEL_EstadoTelefono", Integer)
    employee = Column("FIC_IdEmpleado", Integer, ForeignKey("NOM_FICHA_EMPLEADO.FIC_IdEmpleado"))

    employee_info = relationship("Employee", back_populates="employee_phone")



