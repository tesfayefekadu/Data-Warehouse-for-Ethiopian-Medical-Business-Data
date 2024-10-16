# schemas.py
from pydantic import BaseModel

class ObjectDetectionResultBase(BaseModel):
    image_name: str
    label: str
    x_center: float
    y_center: float
    width: float
    height: float
    confidence: float

class ObjectDetectionResultCreate(ObjectDetectionResultBase):
    pass

class ObjectDetectionResult(ObjectDetectionResultBase):
    detection_id: int

    class Config:
        orm_mode = True
