# 🌐 API Core — VisionCore

API REST transacional do sistema VisionCore. Registra detecções de placas feitas pelos workers e expõe os dados para consulta.

## 🛠️ Stack

| Camada | Tecnologia |
|---|---|
| Framework | FastAPI 0.135 |
| ORM | SQLAlchemy 2.0 |
| Banco | MySQL 8.0 (PyMySQL) |
| Servidor | Uvicorn |
| Infra | Docker + Docker Compose |
| Rede | `parking_global_net` (gerenciada pelo `parking-infra`) |

## 🚀 Como Rodar

> **Pré-requisito:** O `parking-infra` **deve estar rodando** antes da API. Ele cria a rede `parking_global_net`.

### 1. Suba o parking-infra primeiro

```bash
cd ../parking-infra
docker-compose up -d
```

### 2. Configure o `.env`

```bash
cp .env.example .env  # se existir, senão edite o .env diretamente
```

Variáveis necessárias:

| Variável | Descrição |
|---|---|
| `DB_USER` | Usuário MySQL (padrão: `root`) |
| `DB_PASSWORD` | Senha MySQL |
| `DB_NAME` | Nome do banco (padrão: `visioncore`) |

### 3. Suba a API e o MySQL

```bash
docker-compose up -d
```

Isso sobe:
- `visioncore_mysql` — banco de dados na porta **3306**
- `api_core` — API FastAPI na porta **8000** (e via Nginx na porta **80**)

### 4. Verificar

```bash
# Health check direto
curl http://localhost:8000/

# Via Nginx (depois que o parking-infra estiver no ar)
curl http://localhost/api/vagas/registros
```

## 📋 Endpoints

| Método | Rota | Descrição |
|---|---|---|
| `GET` | `/` | Health check |
| `POST` | `/api/vagas/registro` | Registra uma detecção de placa |
| `GET` | `/api/vagas/registros?limit=10` | Lista registros recentes |

## 📁 Estrutura

```
src/
├── main.py
├── core/
│   ├── config.py      # Variáveis de ambiente
│   ├── database.py    # Engine SQLAlchemy
│   └── security.py    # (a implementar)
└── modules/
    └── registros/
        ├── models.py
        ├── schemas.py
        ├── repository.py
        ├── service.py
        └── router.py
```

## 📌 Ordem de inicialização

```
1. parking-infra  → cria a rede e o broker
2. vc-api-core    → este serviço
```
