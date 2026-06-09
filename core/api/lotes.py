from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.validation.database import get_db
import models

router = APIRouter(prefix="/lotes", tags=["lotes"])

@router.post("/")
def criar_lote(lote: dict, db: Session = Depends(get_db)):
    novo = models.Lote(**lote)
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

@router.get("/")
def listar_lotes(db: Session = Depends(get_db)):
    return db.query(models.Lote).all()
