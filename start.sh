#!/usr/bin/env bash

# 1. Aplica as migrações (Cria as tabelas como blog_post)
# Isto corrige o erro: OperationalError: no such table: blog_post
python manage.py migrate

# 2. Inicia o servidor Gunicorn. 
# Adiciona o diretório atual (.) ao PYTHONPATH para que o Gunicorn encontre 'site_natal'.
export PYTHONPATH=$PYTHONPATH:$(pwd)
gunicorn site_natal.wsgi:application