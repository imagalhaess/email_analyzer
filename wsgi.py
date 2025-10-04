#!/usr/bin/env python3
"""
WSGI entry point for the Email Analyzer application.
"""
import sys

# Importa e cria a aplicação
# Gunicorn encontrará o módulo 'app' automaticamente a partir do diretório raiz.
from app import create_app

# Cria a aplicação para WSGI
application = create_app()

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    # O import de 'os' só é necessário aqui
    import os
    print(f"🚀 Iniciando MailMind em modo de desenvolvimento em http://0.0.0.0:{port}")
    application.run(host="0.0.0.0", port=port, debug=False)
