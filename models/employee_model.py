from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from database.database import Base


class Employee(Base):
    __tablename__ = "NOM_FICHA_EMPLEADO"

    key = Column("FIC_IdEmpleado", Integer, primary_key=True, index=True)
    employee_name = Column("FIC_NombreUno", String)
    employee_second_name = Column("FIC_NombreDos", String)
    employee_other_name = Column("FIC_OtrosNombres", String)
    employee_last_name = Column("FIC_ApellidoUno", String)
    employee_second_last_name = Column("FIC_ApellidoDos", String)
    employee_last_name_married = Column("FIC_ApellidoCasada", String)
    employee_dpi = Column("FIC_DpiPasaporte", String)
    employee_born_date = Column("FIC_FechaNacimiento", Date)
    employee_born_place = Column("FIC_LugarNacimiento", String)
    employee_gender = Column("FIC_Genero", String)
    employee_civil_state = Column("FIC_EstadoCivil", String)
    employee_start_date = Column("FIC_FechaIngreso", Date)
    employee_contract = Column("FIC_Contrato", String)
    employee_status = Column("FIC_Estado_Empleado", String)
    job = Column("PUE_IdPuesto", Integer, ForeignKey("NOM_PUESTO.PUE_IdPuesto"))

    employee_phone = relationship("EmployeePhone", back_populates="employee_info")
    employee_email = relationship("Email", back_populates="employee_info")
    employee_address = relationship("Address", back_populates="employee_info")
    employee_item = relationship("EmployeeItem", back_populates="employee_info")
    employee_vacation = relationship("Vacation", back_populates="employee_info")
    employee_hour = relationship("Hour", back_populates="employee_info")
    employee_job = relationship("Job", back_populates="employee_info")
