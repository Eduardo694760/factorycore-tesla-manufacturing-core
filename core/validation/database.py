from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# String de conexão para PostgreSQL
DATABASE_URL = "postgresql+psycopg2://admin:eduardo4@localhost:5432/factorycore"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Função para abrir/fechar sessão do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
