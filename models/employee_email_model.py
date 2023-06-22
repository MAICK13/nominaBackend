from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database.database import Base


class Email(Base):
    __tablename__ = "NOM_CORREO_EMPLEADO"

    key = Column("COR_IdCorreo", Integer, primary_key=True, index=True)
    email_type = Column("COR_TipoDireccion", String)
    employee_email = Column("COR_DireccionEmpleado", String)
    email_indicator = Column("COR_Indicador", String)
    email_status = Column("COR_EstadoCorreo", Integer)
    employee = Column("FIC_IdEmpleado", Integer, ForeignKey("NOM_FICHA_EMPLEADO.FIC_IdEmpleado"))

    employee_info = relationship("Employee", back_populates="employee_email")
