from wsgiref.simple_server import make_server
from my_framework.main import Framework
from views import routes
from components import settings

# Создаем объект WSGI-приложения
application = Framework(settings, routes)

with make_server('', 8003, application) as httpd:
    print("Запуск на порту 8085...")
    httpd.serve_forever()
