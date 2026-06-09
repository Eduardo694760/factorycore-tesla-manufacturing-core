from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.validation.database import get_db
import models

router = APIRouter(prefix="/pecas", tags=["pecas"])

@router.post("/")
def criar_peca(peca: dict, db: Session = Depends(get_db)):
    nova = models.Peca(**peca)
    db.add(nova)
    db.commit()
    db.refresh(nova)
    return nova

@router.get("/")
def listar_pecas(db: Session = Depends(get_db)):
    return db.query(models.Peca).all()
