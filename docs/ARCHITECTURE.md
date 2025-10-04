# Arquitetura - MailMind

## Visão Geral

Sistema de análise de emails usando IA (Google Gemini) para classificar emails como produtivos ou improdutivos e executar ações automáticas.

## Arquitetura Simples

```
Frontend (HTML/CSS/JS) → Flask App → Gemini AI
                           ↓
                    Email Sender (SMTP)
```

## Componentes Principais

### 1. **Flask App** (`app/app.py`)

- Rotas HTTP e interface web
- Orquestração geral do sistema

### 2. **Serviços** (`app/services/`)

- `email_analyzer.py` - Lógica de análise de emails

### 3. **Provedores** (`app/providers/`)

- `gemini_client.py` - Cliente Google Gemini

### 4. **Utilitários** (`app/utils/`)

- `text_preprocess.py` - Pré-processamento de texto
- `email_sender.py` - Envio de emails

## Fluxo de Dados

1. **Recebimento**: Email via interface web ou webhook
2. **Pré-processamento**: Limpeza e tokenização
3. **Análise**: Gemini classifica como produtivo/improdutivo
4. **Ação**:
   - Improdutivo → Resposta automática
   - Produtivo → Encaminhamento para curadoria

## Padrões Utilizados

- **Separation of Concerns**: Cada módulo tem responsabilidade específica
- **Dependency Injection**: Configurações injetadas nos serviços
- **Provider Pattern**: Cliente Gemini abstrai API externa
- **Service Layer**: Lógica de negócio encapsulada

## Configuração

Todas as configurações via variáveis de ambiente (`.env`):

- `GEMINI_API_KEY` - Chave da API
- `SMTP_*` - Configurações de email
- `CURATOR_ADDRESS` - Email para curadoria

---

**Última atualização**: 04/10/2025
