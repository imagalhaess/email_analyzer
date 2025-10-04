#!/usr/bin/env python3
"""
WSGI entry point for the Email Analyzer application.
"""
import sys
import os

# Adiciona o diretório atual ao Python path
sys.path.insert(0, os.path.dirname(__file__))

# Importa e cria a aplicação
from app import create_app

# Cria a aplicação para WSGI
application = create_app()

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    # O import de 'os' só é necessário aqui
    import os
    print(f"🚀 Iniciando MailMind em modo de desenvolvimento em http://0.0.0.0:{port}")
    application.run(host="0.0.0.0", port=port, debug=False)
