from os import path
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
STATIC_FILES_DIR = path.join(ROOT_DIR, 'staticfiles')
STATIC_URL = '/static/'


PORT = 8005
URL_ADDRESS = 'http://127.0.0.1'


# TEMPLATES = [
#     {
#         'BACKEND': 'jinja2',
#         'DIRS': ['templates']
#         ,
#         'APP_DIRS': True,
#     },
# ]