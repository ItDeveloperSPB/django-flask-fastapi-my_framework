# Запуск проекта на django
- 1. gunicorn -w 5 —bind 0.0.0.0:8085 {my_project}.wsgi:application
- 2. python -m uvicorn {my_project}.asgi:application  

# Запуск проекта на  flask
- 1. gunicorn -w 8 -b 0.0.0.0:8085 '{main}:app'

# Запуск проекта на  fastApi
- 1. uvicorn main:app --host 0.0.0.0 --port 8085 --workers=8

# Запуск проекта на  my_framewrok
- 1. gunicorn --workers=5 --bind 0.0.0.0:8085 run:application

# Запуск тестирования полезная информация
- https://russianblogs.com/article/55621406845/
- wrk -t8 -c100 -d5s http://127.0.0.1:8085