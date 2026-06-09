FactoryCore - Núcleo de Fabricação da Tesla 🚗
📌 Objetivo
Núcleo central de validação e controle da fábrica Tesla Manufacturing Core.
Garantir rastreabilidade, confiabilidade e bloqueio imediato em caso de falhas.

📌 Roadmap de Desenvolvimento
Fase 1: Planejamento e Arquitetura ✅ concluída

Fase 2: Organização do Projeto ✅ concluída

Fase 3: Modelagem do Banco de Dados ✅ concluída

Fase 4: Microsserviço de Telemetria ⚠️ em andamento

Fase 5: Motor de Validação ⚠️ em andamento

Fase 6: Gerenciador de Produção ⚠️ em andamento

Fase 7: API REST ✅ concluída

Fase 8: Segurança ✅ parcialmente concluída

Fase 9: Testes ✅ concluída

Fase 10: Documentação e GitHub ✅ concluída

Fase 11: Melhorias Futuras 🚧 planejada

📌 Pilha Tecnológica
Python 3.11+ / FastAPI

MQTT Mosquitto

PostgreSQL

SQLAlchemy / Pydantic

Uvicorn

📌 Configuração do Ambiente
bash
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
📌 Padrão de Commits
Adote um padrão para manter o histórico limpo:

feat: → nova funcionalidade

fix: → correção de bug

docs: → documentação

chore: → tarefas de manutenção

test: → testes

Exemplo:

bash
git commit -m "feat: adicionar módulo de telemetria"
📌 Diagrama ER
Código
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
📌 Endpoints Principais
GET /operadores → listar operadores

POST /operadores → criar operador

PUT /operadores/{id} → atualizar operador

DELETE /operadores/{id} → remover operador

GET /maquinas → listar máquinas

POST /maquinas → criar máquina

GET /lotes → listar lotes

POST /lotes → criar lote

GET /pecas → listar peças

POST /pecas → criar peça

GET /logs → listar logs de erro

POST /logs → criar log de erro

📌 Fluxo Validado
Operador → cadastrado

Máquina → vinculada ao operador

Lote → criado

Peça → vinculada ao lote

Log de erro → vinculado à peça