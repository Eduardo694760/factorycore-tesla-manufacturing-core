# Arquitetura do FactoryCore

## Módulos
- Telemetry: ingestão de dados via MQTT
- Validation: motor de regras
- Production: controle da linha
- Logs: auditoria e rastreabilidade
- API: interface REST

## Fluxo
1. Dados chegam via Telemetry
2. Passam pelo Validation
3. Se aprovados → Production
4. Se reprovados → Logs + bloqueio
