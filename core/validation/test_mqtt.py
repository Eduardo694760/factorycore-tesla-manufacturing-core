import json
from core.validation.database import SessionLocal, Base, engine
from core.validation.models import EventoTelemetry

def init_db():
    Base.metadata.create_all(bind=engine)

def main():
    init_db()
    db = SessionLocal()

    # Simulação de mensagem MQTT
    mqtt_payload = json.dumps({"temperatura": 90, "unidade": "°C"})
    evento = EventoTelemetry(maquina_id=1, tipo="Temperatura", valor=90.0, unidade="°C", payload=mqtt_payload)
    db.add(evento)
    db.commit()
    db.refresh(evento)

    print("Evento MQTT registrado:", evento.tipo, "=", evento.valor, evento.unidade)

if __name__ == "__main__":
    main()
