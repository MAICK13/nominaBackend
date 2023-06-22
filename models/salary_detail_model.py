from sqlalchemy import Column, Integer, ForeignKey, Float

from database.database import Base


class SalaryDetail(Base):
    __tablename__ = "NOM_SALARIO_DETALLE"

    key = Column("SAD_IdSalario", Integer, primary_key=True, index=True)
    salary_correlative = Column("SAD_Correlativo", Integer)
    salary_item = Column("SAD_Rubro", Integer)
    salary_mto = Column("SAD_MTO", Float)
    salary_status = Column("SAD_Estado", Integer)

    salary = Column("SAL_IdSalario", Integer, ForeignKey("SAL_IdSalario.SAL_IdSalario"))
