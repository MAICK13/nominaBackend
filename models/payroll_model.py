from sqlalchemy import Column, Integer, String, ForeignKey, Float

from database.database import Base


class Payroll(Base):
    __tablename__ = "nom_detalle_planilla"

    key = Column("PUE_IdPuesto", Integer, primary_key=True, index=True)
    job_name = Column("PUE_Nombre", String)
    job_description = Column("PUE_Descripcion", String)
    job_status = Column("PUE_Estado", Integer)
    job_salary = Column("PUE_Salario", Float)
    area = Column("ARE_IdArea", Integer, ForeignKey("NOM_AREA.ARE_IdArea"))

    employee_info = relationship("Employee", back_populates="employee_job")
    area_info = relationship("Area", back_populates="job_info")



