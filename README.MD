# Запуск проекта на django
- 1. gunicorn -w 5 —bind 0.0.0.0:8000 {my_project}.wsgi:application
- 2. python -m uvicorn {my_project}.asgi:application  

# Запуск проекта на  flask
- 1. gunicorn -w 5 -b 0.0.0.0:8019 '{main}:app'

# Запуск проекта на  fastApi
- 1. gunicorn -w 5 -b 0.0.0.0:8019 '{main}:app'

# Запуск проекта на  my_framewrok
- 1. gunicorn --workers=5 --bind 0.0.0.0:8077 run:application