from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from database.database import Base


class Vacation(Base):
    __tablename__ = "NOM_VACACIONES"

    key = Column("VAC_IdVacacion", Integer, primary_key=True, index=True)
    request_date = Column("VAC_FecSolicitud", Date)
    start_date = Column("VAC_FecInicio", Date)
    end_date = Column("VAC_FecFin", Date)
    left_days = Column("VAC_DiasAusencia", Integer)
    vacation_status = Column("VAC_Estado", Integer)
    date_approval = Column("VAC_FecAprobacion", Date)
    date_rejection = Column("VAC_FecRechazo", Date)
    rejection_reason = Column("VAC_MotivoRechazo", String)

    employee = Column("FIC_IdEmpleado", Integer, ForeignKey("NOM_FICHA_EMPLEADO.FIC_IdEmpleado"))

    employee_info = relationship("Employee", back_populates="employee_vacation")



