from sqlalchemy.orm import Session
from my_project import models, schemas

def get_detection_results(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.ObjectDetectionResult).offset(skip).limit(limit).all()

def create_detection_result(db: Session, detection: schemas.ObjectDetectionResultCreate):
    db_detection = models.ObjectDetectionResult(**detection.dict())
    db.add(db_detection)
    db.commit()
    db.refresh(db_detection)
    return db_detection
