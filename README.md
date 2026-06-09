# FactoryCore - Tesla Manufacturing Core

## Objetivo
Núcleo central de validação e controle da fábrica Tesla Manufacturing Core.  
Garante rastreabilidade, confiabilidade e bloqueio imediato em caso de falhas.

## Roadmap
- Fase 1: Planejamento e Arquitetura ✅
- Fase 2: Organização do Projeto (em andamento)
- Fase 3: Modelagem do Banco de Dados
- Fase 4: Implementação dos Microsserviços
...

## Stack Tecnológica
- Python 3.11+ / FastAPI
- MQTT (Mosquitto)
- PostgreSQL
- SQLAlchemy / Pydantic
- Uvicorn

## Setup
```bash
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt


---

## 📌 Passo 7 — Definir padrão de commits
Adote um padrão para manter o histórico limpo:
- `feat:` → nova funcionalidade  
- `fix:` → correção de bug  
- `docs:` → documentação  
- `chore:` → tarefas de manutenção  
- `test:` → testes  

Exemplo:
```powershell
git commit -m "feat: adicionar módulo de telemetria"

Diagrama ER
Operador
   │
   └────── opera ──────► Máquina
                              │
                              │ gera
                              ▼
                     EventoTelemetry


Lote
  │
  └──── contém ─────► Peça
                            │
                            │ possui
                            ▼
                         LogErro