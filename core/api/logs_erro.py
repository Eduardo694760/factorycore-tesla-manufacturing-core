from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.validation.database import get_db
import models

router = APIRouter(prefix="/logs_erro", tags=["logs_erro"])

@router.post("/")
def criar_log(log: dict, db: Session = Depends(get_db)):
    novo = models.LogErro(**log)
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

@router.get("/")
def listar_logs(db: Session = Depends(get_db)):
    return db.query(models.LogErro).all()
