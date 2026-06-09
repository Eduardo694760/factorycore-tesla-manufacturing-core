from core.validation.database import SessionLocal, Base, engine
from core.validation.models import Operador, Maquina, EventoTelemetry

def init_db():
    Base.metadata.create_all(bind=engine)

def main():
    init_db()
    db = SessionLocal()

    operador = Operador(nome="Carlos", matricula="OP123", turno="Manhã")
    db.add(operador)
    db.commit()
    db.refresh(operador)

    maquina = Maquina(codigo="M001", nome="RobotX", status="ativa", operador_id=operador.id)
    db.add(maquina)
    db.commit()
    db.refresh(maquina)

    evento = EventoTelemetry(maquina_id=maquina.id, tipo="Temperatura", valor=85.0, unidade="°C")
    db.add(evento)
    db.commit()
    db.refresh(evento)

    print("Operador:", operador.nome)
    print("Máquina:", maquina.nome)
    print("Evento:", evento.tipo, "=", evento.valor, evento.unidade)

if __name__ == "__main__":
    main()
