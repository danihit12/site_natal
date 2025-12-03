#!/usr/bin/env bash

# 1. Aplica as migrações (CRIA AS TABELAS)
python manage.py migrate

# 2. Inicia o servidor Gunicorn (Substitua "meu_novo_site" pelo nome da sua pasta principal do projeto Django)
gunicorn meu_novo_site.wsgi:application