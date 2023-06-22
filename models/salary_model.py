from sqlalchemy import Column, Integer, String, Date, ForeignKey

from database.database import Base


class Salary(Base):
    __tablename__ = "SAL_IdSalario"

    key = Column("SAL_IdSalario", Integer, primary_key=True, index=True)
    pay_date = Column("SAL_FecPago", Date)
    salary_status = Column("SAL_Estado", Integer)
    employee = Column("FIC_IdEmpleado", Integer, ForeignKey("NOM_FICHA_EMPLEADO.FIC_IdEmpleado"))



