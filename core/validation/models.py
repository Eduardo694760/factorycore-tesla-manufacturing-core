from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy import Column, Integer, String, DateTime, func
from core.validation.database import Base
from .database import Base


class Operador(Base):
    __tablename__ = "operadores"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    matricula = Column(String, unique=True, nullable=False)
    turno = Column(String, nullable=False)
    criado_em = Column(DateTime(timezone=True), server_default=func.now())

    # Relacionamento 1:N com máquinas
    maquinas = relationship("Maquina", back_populates="operador")


class Maquina(Base):
    __tablename__ = "maquinas"

    id = Column(Integer, primary_key=True, index=True)  # Identificador único
    codigo = Column(String(80), unique=True, index=True, nullable=False)  # Código único da máquina
    nome = Column(String(120), nullable=False)  # Nome da máquina
    status = Column(String(50), nullable=False, default="ativa")  # Status da máquina
    operador_id = Column(Integer, ForeignKey("operadores.id"), nullable=False)  # FK para Operador
    criado_em = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)  # Data de criação automática

    operador = relationship("Operador", back_populates="maquinas")  # Máquina pertence a um operador
    eventos_telemetry = relationship("EventoTelemetry", back_populates="maquina")  # Relacionamento 1:N com eventos


class EventoTelemetry(Base):
    __tablename__ = "eventos_telemetry"

    id = Column(Integer, primary_key=True, index=True)  # Identificador único
    maquina_id = Column(Integer, ForeignKey("maquinas.id"), nullable=False)  # FK para Máquina
    tipo = Column(String(80), nullable=False)  # Tipo de evento (ex: temperatura, pressão)
    valor = Column(Float, nullable=True)  # Valor numérico do evento
    unidade = Column(String(30), nullable=True)  # Unidade de medida (ex: °C, bar)
    payload = Column(Text, nullable=True)  # Dados adicionais em texto
    registrado_em = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)  # Data de registro automática

    maquina = relationship("Maquina", back_populates="eventos_telemetry")  # Evento pertence a uma máquina


class Lote(Base):
    __tablename__ = "lotes"

    id = Column(Integer, primary_key=True, index=True)  # Identificador único
    codigo = Column(String(80), unique=True, index=True, nullable=False)  # Código único do lote
    produto = Column(String(120), nullable=False)  # Produto associado ao lote
    status = Column(String(50), nullable=False, default="aberto")  # Status do lote
    criado_em = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)  # Data de criação automática

    pecas = relationship("Peca", back_populates="lote")  # Relacionamento 1:N com peças


class Peca(Base):
    __tablename__ = "pecas"

    id = Column(Integer, primary_key=True, index=True)  # Identificador único
    numero_serie = Column(String(100), unique=True, index=True, nullable=False)  # Número de série único
    lote_id = Column(Integer, ForeignKey("lotes.id"), nullable=False)  # FK para Lote
    status = Column(String(50), nullable=False, default="pendente")  # Status da peça
    criado_em = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)  # Data de criação automática

    lote = relationship("Lote", back_populates="pecas")  # Peça pertence a um lote
    logs_erro = relationship("LogErro", back_populates="peca")  # Relacionamento 1:N com logs de erro


class LogErro(Base):
    __tablename__ = "logs_erro"

    id = Column(Integer, primary_key=True, index=True)  # Identificador único
    peca_id = Column(Integer, ForeignKey("pecas.id"), nullable=False)  # FK para Peça
    codigo = Column(String(80), index=True, nullable=False)  # Código do erro
    mensagem = Column(Text, nullable=False)  # Mensagem descritiva do erro
    severidade = Column(String(50), nullable=False, default="erro")  # Nível de severidade
    registrado_em = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)  # Data de registro automática

    peca = relationship("Peca", back_populates="logs_erro")  # Log pertence a uma peça
