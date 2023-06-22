from sqlalchemy.orm import Session

import models.employee_item_model as employee_item_model
import models.employee_item_dto as employee_item_dto


def get_employee_item(db: Session, skip: int = 0, limit: int = 1000):

    rows = db.query(employee_item_model.EmployeeItem).filter(employee_item_model.EmployeeItem.item_status == 1)\
       .join(employee_item_model.EmployeeItem.employee_info).join(employee_item_model.EmployeeItem.item_info)\
       .offset(skip).limit(limit).all()

    results = []
    for employee_item_row in rows:
        result = employee_item_dto.EmployeeItemResult(
            employee_name=employee_item_row.employee_info.employee_name+ " "
                          +employee_item_row.employee_info.employee_last_name,
            item=employee_item_row.item_info.item_description,
            item_mont=employee_item_row.item_mont,
            item_fact=employee_item_row.item_fact,
            key=employee_item_row.key
        )
        results.append(result)

    return results


def get_employee_item_by_id(db, employee_item_id):
    return db.query(employee_item_model.EmployeeItem).filter(employee_item_model.EmployeeItem.key == employee_item_id,
                                                             employee_item_model.EmployeeItem.item_status == 1).first()


def create_employee_item(db: Session, employee_item_create: employee_item_dto.EmployeeItemCreate):

    exist_item = db.query(employee_item_model.EmployeeItem).filter(
        employee_item_model.EmployeeItem.employee == employee_item_create.employee,
        employee_item_model.EmployeeItem.item == employee_item_create.item,
        employee_item_model.EmployeeItem.item_status == 1).first()

    if exist_item is not None:
        return False

    db_item = employee_item_model.EmployeeItem(item_status=1, employee=employee_item_create.employee,
                                               item=employee_item_create.item,
                                               item_mont=employee_item_create.item_mont,
                                               item_fact=employee_item_create.item_fact)

    db.add(db_item)
    db.commit()
    db.refresh(db_item)

    return db_item


def update_employee_item(db: Session, employee_item_id: int,
                         employee_item_update: employee_item_dto.EmployeeItemUpdate):

    db_item = db.get(employee_item_model.EmployeeItem, employee_item_id)

    if not db_item:
        return db_item

    employee_item_data = employee_item_update.dict(exclude_unset=True)

    for key, value in employee_item_data.items():
        setattr(db_item, key, value)

    db.add(db_item)
    db.commit()
    db.refresh(db_item)

    return db_item


def delete_employee_item(db, employee_item_id):

    db_item = db.get(employee_item_model.EmployeeItem, employee_item_id)

    setattr(db_item, 'item_status', 0)

    db.add(db_item)
    db.commit()
    db.refresh(db_item)

    return db_item
