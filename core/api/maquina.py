from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.validation.database import get_db
import models

router = APIRouter(prefix="/maquinas", tags=["maquinas"])

@router.post("/")
def criar_maquina(maquina: dict, db: Session = Depends(get_db)):
    nova = models.Maquina(**maquina)
    db.add(nova)
    db.commit()
    db.refresh(nova)
    return nova

@router.get("/")
def listar_maquinas(db: Session = Depends(get_db)):
    return db.query(models.Maquina).all()
