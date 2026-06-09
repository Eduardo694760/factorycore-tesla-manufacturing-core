from core.validation.database import SessionLocal, Base, engine
from core.validation.models import Operador, Maquina, EventoTelemetry, Lote, Peca, LogErro

def init_db():
    # Cria as tabelas se não existirem
    Base.metadata.create_all(bind=engine)

def main():
    init_db()
    db = SessionLocal()

    # 1. Criar Operador
    operador = Operador(nome="Eduardo", matricula="OP999", turno="Noite")
    db.add(operador)
    db.commit()
    db.refresh(operador)

    # 2. Criar Máquina vinculada ao Operador
    maquina = Maquina(codigo="MX100", nome="Prensa Hidráulica", status="ativa", operador_id=operador.id)
    db.add(maquina)
    db.commit()
    db.refresh(maquina)

    # 3. Registrar EventoTelemetry da Máquina
    evento = EventoTelemetry(maquina_id=maquina.id, tipo="Pressão", valor=120.5, unidade="bar")
    db.add(evento)
    db.commit()
    db.refresh(evento)

    # 4. Criar Lote
    lote = Lote(codigo="L20260608", produto="ComponenteX")
    db.add(lote)
    db.commit()
    db.refresh(lote)

    # 5. Criar Peça vinculada ao Lote
    peca = Peca(numero_serie="PX123456", lote_id=lote.id, status="pendente")
    db.add(peca)
    db.commit()
    db.refresh(peca)

    # 6. Registrar LogErro da Peça
    erro = LogErro(peca_id=peca.id, codigo="E404", mensagem="Falha de calibração", severidade="grave")
    db.add(erro)
    db.commit()
    db.refresh(erro)

    # 7. Imprimir resultados
    print("Operador:", operador.nome, "-", operador.matricula)
    print("Máquina:", maquina.nome, "-", maquina.codigo)
    print("Evento:", evento.tipo, "=", evento.valor, evento.unidade)
    print("Lote:", lote.codigo, "-", lote.produto)
    print("Peça:", peca.numero_serie, "-", peca.status)
    print("Erro:", erro.codigo, "-", erro.mensagem)

if __name__ == "__main__":
    main()
