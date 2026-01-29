#!/usr/bin/env python

"""
Django SECRET_KEY generator.
"""
import os
from django.utils.crypto import get_random_string

chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'

CONFIG_STRING = """
DEBUG=True
SECRET_KEY=%s
ALLOWED_HOSTS=127.0.0.1, .localhost
""".strip() % get_random_string(50, chars)

# Writing our configuration file to '.env'
if not os.path.exists('.env'):
    with open('.env', 'w') as configfile:
        configfile.write(CONFIG_STRING)
    print("Arquivo .env criado com sucesso!")
else:
    print(".env já existe. Nenhuma alteração foi feita.")
