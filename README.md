# API Core
Este repositório contém o núcleo transacional e a lógica de negócio do sistema de monitoramento de estacionamento baseado em Visão Computacional. A **API Core** é responsável pela gestão de dados, autenticação e coordenação dos fluxos de eventos entre a portaria e o pátio.

## 🚀 Tecnologias Principais

-   **Framework:** FastAPI (Python) para alta performance assíncrona.
    
-   **Banco de Dados:** PostgreSQL (Interface via SQLAlchemy ORM) para garantir integridade ACID.
    
-   **Mensageria:** Redis (Broker) para distribuição de tarefas aos Workers.
    
-   **Segurança/Infra:** Nginx como Proxy Reverso e Docker para conteinerização.

## 🏗️ Responsabilidades do Módulo

1.  **Gestão de Dados (CRUD):** Cadastro de usuários, veículos autorizados e mapeamento de polígonos das vagas.
    
2.  **Regras de Negócio:** Validação de acesso, cálculos de permanência com precisão de milissegundos e auditoria.
    
3.  **Comunicação em Tempo Real:** Emissão de alertas via WebSockets para a interface da guarita em casos de necessidade de revisão manual.
    
4.  **Integração de Mensageria:** Recebimento de resultados do **Worker Portaria** e **Worker Pátio** através das filas do Redis.
