from sqlalchemy.orm import Session

import models.employee_address_model as employee_address_model
import models.employee_address_dto as employee_address_dto


def get_employee_address(db: Session, skip: int = 0, limit: int = 1000):
    rows = db.query(employee_address_model.Address).filter(employee_address_model.Address.address_status == 1)\
        .join(employee_address_model.Address.employee_info).offset(skip).limit(limit).all()

    results = []
    for employee_address_row in rows:
        result = employee_address_dto.AddressResult(
            address_type=employee_address_row.address_type,
            employee_address=employee_address_row.employee_address,
            employee_name=employee_address_row.employee_info.employee_name+ " "
                          +employee_address_row.employee_info.employee_last_name,
            key=employee_address_row.key
        )
        results.append(result)

    return results


def get_employee_address_by_id(db, employee_address_id):
    return db.query(employee_address_model.Address).filter(employee_address_model.Address.key == employee_address_id,
                                                           employee_address_model.Address.address_status == 1).first()


def create_employee_address(db: Session, employee_address_create: employee_address_dto.AddressCreate):

    exist_address = db.query(employee_address_model.Address).filter(
        employee_address_model.Address.address_type == employee_address_create.address_type,
        employee_address_model.Address.employee_address == employee_address_create.employee_address,
        employee_address_model.Address.employee == employee_address_create.employee,
        employee_address_model.Address.address_status == 1).first()

    if exist_address is not None:
        return False

    db_address = employee_address_model.Address(address_type=employee_address_create.address_type,
                                                employee_address=employee_address_create.employee_address,
                                                address_indicator=employee_address_create.address_indicator,
                                                address_status=1, employee=employee_address_create.employee)

    db.add(db_address)
    db.commit()
    db.refresh(db_address)

    return db_address


def update_employee_address(db: Session, employee_address_id: int,
                            employee_address_update: employee_address_dto.AddressUpdate):
    db_address = db.get(employee_address_model.Address, employee_address_id)

    if not db_address:
        return db_address

    employee_phone_data = employee_address_update.dict(exclude_unset=True)

    for key, value in employee_phone_data.items():
        setattr(db_address, key, value)

    db.add(db_address)
    db.commit()
    db.refresh(db_address)

    return db_address


def delete_employee_address(db, employee_address_id):

    db_address = db.get(employee_address_model.Address, employee_address_id)

    setattr(db_address, 'address_status', 0)

    db.add(db_address)
    db.commit()
    db.refresh(db_address)

    return db_address
