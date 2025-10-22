from pydantic import BaseModel

class WorkerBase(BaseModel):
    name: str

class WorkerOut(WorkerBase):
    id: int
    class Config:
        from_attributes = True
        
        