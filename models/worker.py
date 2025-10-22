from sqlalchemy import Column, String, Integer
from db.base import Base

class Worker(Base):
    __tablename__ = 'workers'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)