from sqlalchemy.orm import Session

import models.item_model as item_model
import models.item_dto as item_dto


def get_items(db: Session, skip: int = 0, limit: int = 1000):
    return db.query(item_model.Item).filter(item_model.Item.item_status == 1).offset(skip).limit(limit).all()


def get_item_by_id(db, vacation_id):
    return db.query(item_model.Item).filter(item_model.Item.key == vacation_id,
                                            item_model.Item.item_status == 1).first()


def create_item(db: Session, item_create: item_dto.ItemCreate):

    exist_item = db.query(item_model.Item).filter(
        item_model.Item.item_description == item_create.item_description,
        item_model.Item.item_type == item_create.item_type,
        item_model.Item.item_status == 1).first()

    if exist_item is not None:
        return False

    db_item = item_model.Item(item_description=item_create.item_description, item_type=item_create.item_type,
                              item_status=1)

    db.add(db_item)
    db.commit()
    db.refresh(db_item)

    return db_item


def update_item(db: Session, item_id: int, item_update: item_dto.ItemUpdate):
    db_item = db.get(item_model.Item, item_id)

    if not db_item:
        return db_item

    item_data = item_update.dict(exclude_unset=True)

    for key, value in item_data.items():
        setattr(db_item, key, value)

    db.add(db_item)
    db.commit()
    db.refresh(db_item)

    return db_item


def delete_item(db, item_id):

    db_item = db.get(item_model.Item, item_id)

    setattr(db_item, 'item_status', 0)

    db.add(db_item)
    db.commit()
    db.refresh(db_item)

    return db_item
