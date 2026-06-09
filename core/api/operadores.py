from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.validation.database import get_db
from core.validation import models
from pydantic import BaseModel

router = APIRouter(prefix="/operadores", tags=["Operadores"])

class OperadorCreate(BaseModel):
    nome: str
    matricula: str
    turno: str

@router.get("/")
def listar_operadores(db: Session = Depends(get_db)):
    return db.query(models.Operador).all()

@router.post("/")
def criar_operador(op: OperadorCreate, db: Session = Depends(get_db)):
    novo = models.Operador(**op.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

