from sqlalchemy.orm import Session
from db.session import get_db
from fastapi import APIRouter, Depends
from models.worker import Worker
from schemas.worker import WorkerBase, WorkerOut


router = APIRouter(prefix='/worker')

@router.post('/', response_model= WorkerOut)
def create_worker(user_data: WorkerBase, db: Session = Depends(get_db) ):
    new_worker = Worker(name = user_data.name)
    db.add(new_worker)
    db.commit()
    db.refresh(new_worker)
    return new_worker