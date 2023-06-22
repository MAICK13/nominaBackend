import os
import pandas as pd
from sqlalchemy.orm import Session
from services import area_service, job_service, employee_phone_service, employee_email_service,\
    employee_address_service, employee_item_service, item_service, vacation_service, employee_service, hour_service

from models import report_dto

from sqlalchemy import text

reports_path = os.path.dirname(os.path.abspath(' ')) + "/src/reports/"


def verify_file_exist(file_name):
    path = os.path.join(reports_path, file_name)

    if os.path.exists(path):
        os.remove(path)


def get_areas_report(db: Session):
    report_name = "reporte_areas.xlsx"

    verify_file_exist(report_name)

    areas = area_service.get_areas(db)

    df = pd.DataFrame([t.__dict__ for t in areas])
    df = df.drop(columns=['_sa_instance_state'])
    df.to_excel(reports_path + report_name, index=None)

    return os.path.join(reports_path, report_name)


def get_job_report(db: Session):
    report_name = "reporte_puestos.xlsx"

    verify_file_exist(report_name)

    jobs = job_service.get_jobs(db)

    df = pd.DataFrame([t.__dict__ for t in jobs])
    df = df.drop(columns=['_sa_instance_state'])
    df.to_excel(reports_path + report_name, index=None)

    return os.path.join(reports_path, report_name)


def get_employee_phone(db: Session):
    report_name = "reporte_telefono_empleado.xlsx"

    verify_file_exist(report_name)

    jobs = employee_phone_service.get_employee_phone(db)

    df = pd.DataFrame([t.__dict__ for t in jobs])
    # df = df.drop(columns=['_sa_instance_state'])
    df.to_excel(reports_path + report_name, index=None)

    return os.path.join(reports_path, report_name)


def get_employee_email(db: Session):
    report_name = "reporte_email_empleado.xlsx"

    verify_file_exist(report_name)

    jobs = employee_email_service.get_employee_email(db)

    df = pd.DataFrame([t.__dict__ for t in jobs])
    # df = df.drop(columns=['_sa_instance_state'])
    df.to_excel(reports_path + report_name, index=None)

    return os.path.join(reports_path, report_name)


def get_employee_address(db: Session):
    report_name = "reporte_direccion_empleado.xlsx"

    verify_file_exist(report_name)

    jobs = employee_address_service.get_employee_address(db)

    df = pd.DataFrame([t.__dict__ for t in jobs])
    # df = df.drop(columns=['_sa_instance_state'])
    df.to_excel(reports_path + report_name, index=None)

    return os.path.join(reports_path, report_name)


def get_employee_item(db: Session):
    report_name = "reporte_rubro_empleado.xlsx"

    verify_file_exist(report_name)

    jobs = employee_item_service.get_employee_item(db)

    df = pd.DataFrame([t.__dict__ for t in jobs])
    # df = df.drop(columns=['_sa_instance_state'])
    df.to_excel(reports_path + report_name, index=None)

    return os.path.join(reports_path, report_name)


def get_item(db: Session):
    report_name = "reporte_rubros.xlsx"

    verify_file_exist(report_name)

    jobs = item_service.get_items(db)

    df = pd.DataFrame([t.__dict__ for t in jobs])
    df = df.drop(columns=['_sa_instance_state'])
    df.to_excel(reports_path + report_name, index=None)

    return os.path.join(reports_path, report_name)


def get_vacation(db: Session):
    report_name = "reporte_vacaciones.xlsx"

    verify_file_exist(report_name)

    jobs = vacation_service.get_vacations(db)

    df = pd.DataFrame([t.__dict__ for t in jobs])
    df = df.drop(columns=['_sa_instance_state'])
    df.to_excel(reports_path + report_name, index=None)

    return os.path.join(reports_path, report_name)


def get_employees(db: Session):
    report_name = "reporte_empleados.xlsx"

    verify_file_exist(report_name)

    jobs = employee_service.get_employees(db)

    df = pd.DataFrame([t.__dict__ for t in jobs])
    df = df.drop(columns=['_sa_instance_state'])
    df.to_excel(reports_path + report_name, index=None)

    return os.path.join(reports_path, report_name)


def get_hours(db: Session):
    report_name = "reporte_horas.xlsx"

    verify_file_exist(report_name)

    jobs = hour_service.get_hours(db)

    df = pd.DataFrame([t.__dict__ for t in jobs])
    df = df.drop(columns=['_sa_instance_state'])
    df.to_excel(reports_path + report_name, index=None)

    return os.path.join(reports_path, report_name)


def get_payroll(payroll_data: report_dto.PayrollCreate, db: Session):
    report_name = "reporte_nomina.xlsx"

    db.execute(text("delete from nom_detalle_planilla;"))
    db.commit()

    if payroll_data.type == '1':

        db.execute(text(f"CALL detalle_planilla_quincena('{payroll_data.start_date}',"
                        f" '{payroll_data.end_date}', '{payroll_data.pay_date}');"))
        db.commit()
    else:
        db.execute(text(f"CALL detalle_planilla_finmes('{payroll_data.start_date}',"
                        f" '{payroll_data.end_date}', '{payroll_data.pay_date}');"))
        db.commit()

    query = text("select NFE.FIC_NombreUno as nombre, NFE.FIC_ApellidoUno as apellido, nep.ENC_FechaInicio as fecha_inicio, nep.ENC_FechaFin as fecha_fin, NR.RUB_Descripcion as rubro, dp.RUB_Monto as monto from nom_detalle_planilla dp INNER JOIN nom_encabezado_planilla nep on dp.ENC_idEncabezado = nep.ENC_idEncabezado INNER JOIN NOM_FICHA_EMPLEADO NFE on dp.FIC_IdEmpleado = NFE.FIC_IdEmpleado INNER JOIN NOM_RUBRO NR on dp.RUB_IdRubro = NR.RUB_IdRubro;")
    rows = db.execute(query)

    results = []
    for payroll in rows:
        result = report_dto.PayrollResult(
            name=payroll[0],
            last_name=payroll[1],
            start_date=str(payroll[2]),
            end_date=str(payroll[3]),
            item=str(payroll[4]),
            mont=payroll[5]
        )
        results.append(result)

    df = pd.DataFrame([t.__dict__ for t in results])

    print(df)

    total = df['mont'].sum()
    new_row = {'name': 'Total', 'last_name': '', 'start_date': '', 'end_date': '', 'item': '', 'mont': total}
    #df = df.append(new_row, ignore_index=True)
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

    df.to_excel(reports_path + report_name, index=None)

    return os.path.join(reports_path, report_name)


def get_ticket(ticket_data: report_dto.TicketCreate, db: Session):
    report_name = "reporte_boleta.xlsx"

    query = text(
        f"select NFE.FIC_NombreUno as nombre, NFE.FIC_ApellidoUno as apellido, nep.ENC_FechaInicio "
        f"as fecha_inicio, nep.ENC_FechaFin as fecha_fin, NR.RUB_Descripcion as rubro, dp.RUB_Monto "
        f"as monto from nom_detalle_planilla dp INNER JOIN nom_encabezado_planilla nep "
        f"on dp.ENC_idEncabezado = nep.ENC_idEncabezado INNER JOIN NOM_FICHA_EMPLEADO NFE"
        f" on dp.FIC_IdEmpleado = NFE.FIC_IdEmpleado INNER JOIN NOM_RUBRO NR "
        f"on dp.RUB_IdRubro = NR.RUB_IdRubro WHERE NFE.FIC_IdEmpleado={ticket_data.employee};")

    rows = db.execute(query)

    results = []
    for payroll in rows:
        result = report_dto.PayrollResult(
            name=payroll[0],
            last_name=payroll[1],
            start_date=str(payroll[2]),
            end_date=str(payroll[3]),
            item=str(payroll[4]),
            mont=payroll[5]
        )
        results.append(result)

    df = pd.DataFrame([t.__dict__ for t in results])

    total = df['mont'].sum()
    new_row = {'name': 'Total', 'last_name': '', 'start_date': '', 'end_date': '', 'item': '', 'mont': total}
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

    df.to_excel(reports_path + report_name, index=None)

    return os.path.join(reports_path, report_name)
