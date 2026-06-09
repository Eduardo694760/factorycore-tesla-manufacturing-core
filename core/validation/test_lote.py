from core.validation.database import SessionLocal, Base, engine
from core.validation.models import Lote, Peca, LogErro

def init_db():
    Base.metadata.create_all(bind=engine)

def main():
    init_db()
    db = SessionLocal()

    lote = Lote(codigo="L20260608", produto="SensorX")
    db.add(lote)
    db.commit()
    db.refresh(lote)

    peca = Peca(numero_serie="P12345", lote_id=lote.id, status="DEFECT")
    db.add(peca)
    db.commit()
    db.refresh(peca)

    erro = LogErro(peca_id=peca.id, codigo="E001", mensagem="Falha no sensor de pressão", severidade="grave")
    db.add(erro)
    db.commit()
    db.refresh(erro)

    print("Lote:", lote.codigo, "-", lote.produto)
    print("Peça:", peca.numero_serie, "-", peca.status)
    print("Erro:", erro.codigo, "-", erro.mensagem)

if __name__ == "__main__":
    main()
