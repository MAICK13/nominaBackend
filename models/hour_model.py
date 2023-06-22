from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from database.database import Base


class Hour(Base):
    __tablename__ = "NOM_HORAS"

    key = Column("HOR_IdHora", Integer, primary_key=True, index=True)
    start_date = Column("HOR_FecInicio", String)
    end_date = Column("HOR_FecFin", String)
    hour = Column("HOR_Horas", String)
    hour_status = Column("HOR_Estado", Integer)

    employee = Column("FIC_IdEmpleado", Integer, ForeignKey("NOM_FICHA_EMPLEADO.FIC_IdEmpleado"))
    employee_info = relationship("Employee", back_populates="employee_hour")
