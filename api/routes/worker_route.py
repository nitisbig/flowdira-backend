from sqlalchemy.orm import Session
from db.session import get_db
from fastapi import APIRouter, Depends
from models.worker import Worker
from schemas.worker import WorkerBase, WorkerOut
from models.user import User
from api.deps import get_current_user


router = APIRouter(prefix='/worker', tags=["Worker"])

@router.post('/', response_model= WorkerOut)
def create_worker(user_data: WorkerBase, db: Session = Depends(get_db), current_user: User = Depends(get_current_user) ):
    new_worker = Worker(name = user_data.name, owner_id = current_user.id)
    db.add(new_worker)
    db.commit()
    db.refresh(new_worker)
    return new_worker

@router.get('/me', response_model=list[WorkerOut])
def get_all_worker(db: Session=Depends(get_db), current_user: User = Depends(get_current_user)):
    workers = db.query(Worker).filter(Worker.owner_id == current_user.id).all()
    return workers