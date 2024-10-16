from sqlalchemy import Column, Integer, String, Float
from .database import Base

class ObjectDetectionResult(Base):
    __tablename__ = "object_detection_results"

    detection_id = Column(Integer, primary_key=True, index=True)
    image_name = Column(String, index=True)
    label = Column(String)
    x_center = Column(Float)
    y_center = Column(Float)
    width = Column(Float)
    height = Column(Float)
    confidence = Column(Float)