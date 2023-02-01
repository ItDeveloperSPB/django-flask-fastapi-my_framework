from wsgiref.simple_server import make_server

from components.settings import URL_ADDRESS, PORT
from framework_kuzya.main import Framework, DebugApplication, FakeApplication
from views import routes
from components import settings

# Создаем объект WSGI-приложения
application = Framework(settings, routes)
# application = DebugApplication(settings, routes)
# application = FakeApplication(settings, routes)


with make_server('', PORT, application) as httpd:
    print(f'Сервер запущен  {URL_ADDRESS}:{PORT}')
    httpd.serve_forever()
