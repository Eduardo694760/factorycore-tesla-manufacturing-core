from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel

from core.validation.database import SessionLocal, Base, engine
from core.validation import models

app = FastAPI(title="FactoryCore API")

# Criar as tabelas no banco de dados
Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# --- Schemas Pydantic para entrada ---

class OperadorCreate(BaseModel):
    nome: str
    matricula: str
    turno: str


class MaquinaCreate(BaseModel):
    codigo: str
    nome: str
    status: str
    operador_id: int


class LoteCreate(BaseModel):
    codigo: str
    produto: str


class PecaCreate(BaseModel):
    numero_serie: str
    lote_id: int
    status: str


class LogErroCreate(BaseModel):
    peca_id: int
    codigo: str
    mensagem: str
    severidade: str


# --- Endpoints GET ---

@app.get("/operadores")
def listar_operadores(db: Session = Depends(get_db)):
    return db.query(models.Operador).all()


@app.get("/maquinas")
def listar_maquinas(db: Session = Depends(get_db)):
    return db.query(models.Maquina).all()


@app.get("/eventos")
def listar_eventos(db: Session = Depends(get_db)):
    return db.query(models.EventoTelemetry).all()


@app.get("/lotes")
def listar_lotes(db: Session = Depends(get_db)):
    return db.query(models.Lote).all()


@app.get("/pecas")
def listar_pecas(db: Session = Depends(get_db)):
    return db.query(models.Peca).all()


@app.get("/logs")
def listar_logs(db: Session = Depends(get_db)):
    return db.query(models.LogErro).all()


# --- Endpoints PUT ---

@app.put("/operadores/{operador_id}")
def atualizar_operador(
    operador_id: int,
    op: OperadorCreate,
    db: Session = Depends(get_db)
):
    operador = (
        db.query(models.Operador)
        .filter(models.Operador.id == operador_id)
        .first()
    )

    if not operador:
        raise HTTPException(
            status_code=404,
            detail="Operador não encontrado"
        )

    for key, value in op.dict().items():
        setattr(operador, key, value)

    db.commit()
    db.refresh(operador)

    return operador


# --- Endpoints POST ---

@app.post("/operadores")
def criar_operador(op: OperadorCreate, db: Session = Depends(get_db)):
    novo = models.Operador(**op.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo


@app.post("/maquinas")
def criar_maquina(m: MaquinaCreate, db: Session = Depends(get_db)):
    nova = models.Maquina(**m.dict())
    db.add(nova)
    db.commit()
    db.refresh(nova)
    return nova


@app.post("/lotes")
def criar_lote(l: LoteCreate, db: Session = Depends(get_db)):
    novo = models.Lote(**l.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo


@app.post("/pecas")
def criar_peca(p: PecaCreate, db: Session = Depends(get_db)):
    nova = models.Peca(**p.dict())
    db.add(nova)
    db.commit()
    db.refresh(nova)
    return nova


@app.post("/logs")
def criar_logerro(e: LogErroCreate, db: Session = Depends(get_db)):
    novo = models.LogErro(**e.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo


# --- Endpoints DELETE ---

@app.delete("/operadores/{operador_id}")
def deletar_operador(
    operador_id: int,
    db: Session = Depends(get_db)
):
    operador = (
        db.query(models.Operador)
        .filter(models.Operador.id == operador_id)
        .first()
    )

    if not operador:
        raise HTTPException(
            status_code=404,
            detail="Operador não encontrado"
        )

    db.delete(operador)
    db.commit()

    return {
        "message": f"Operador {operador_id} apagado com sucesso"
    }


@app.delete("/maquinas/{maquina_id}")
def deletar_maquina(
    maquina_id: int,
    db: Session = Depends(get_db)
):
    maquina = (
        db.query(models.Maquina)
        .filter(models.Maquina.id == maquina_id)
        .first()
    )

    if not maquina:
        raise HTTPException(
            status_code=404,
            detail="Máquina não encontrada"
        )

    db.delete(maquina)
    db.commit()

    return {
        "message": f"Máquina {maquina_id} apagada com sucesso"
    }


@app.delete("/lotes/{lote_id}")
def deletar_lote(
    lote_id: int,
    db: Session = Depends(get_db)
):
    lote = (
        db.query(models.Lote)
        .filter(models.Lote.id == lote_id)
        .first()
    )

    if not lote:
        raise HTTPException(
            status_code=404,
            detail="Lote não encontrado"
        )

    db.delete(lote)
    db.commit()

    return {
        "message": f"Lote {lote_id} apagado com sucesso"
    }


# --- Endpoint raiz ---

@app.get("/")
def root():
    return {
        "message": "FactoryCore API está rodando 🚀"
    }
