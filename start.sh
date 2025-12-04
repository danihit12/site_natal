#!/usr/bin/env bash

# 1. Aplica as migrações (Corrige o OperationalError)
python manage.py migrate

# 2. Define o PYTHONPATH para incluir o diretório de origem do Render (src)
# Isto garante que o Python encontre 'trabalho2'
export PYTHONPATH=$PYTHONPATH:/opt/render/project/src/

# 3. Inicia o servidor Gunicorn usando o nome correto do módulo
# O comando agora procura por 'trabalho2.wsgi'
gunicorn trabalho2.wsgi:application