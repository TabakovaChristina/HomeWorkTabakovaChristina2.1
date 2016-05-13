# -*- coding: utf-8 -*-
# Pyramid приложение начинается с конфига, который создается при помощи класса Configurator из модуля pyramid.config.
# В дальнейшем экземпляр класса Configurator используется для настройки Pyramid приложения.
from pyramid.config import Configurator
def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.add_static_view('static', 'static', cache_max_age=3600)
# Метод конфигуратора pyramid.config.Configurator.add_route(), регистрирует новый маршрут (route) с названием “index”.
    config.add_route('index', '/')
    config.add_route('aboutme', '/aboutme/aboutme.html')
    config.scan()
# Метод pyramid.config.Configurator.make_wsgi_app() создает WSGI приложение, по тем настройкам которые мы передали в конфигуратор.
    return config.make_wsgi_app()
