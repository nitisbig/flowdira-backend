from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from db.base import Base

class Worker(Base):
    __tablename__ = 'workers'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id", ondelete='CASCADE'))

    owner = relationship("User", back_populates='workers')