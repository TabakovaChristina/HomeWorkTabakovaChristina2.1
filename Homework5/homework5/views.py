# -*- coding: utf-8 -*-
from pyramid.view import view_config

#@view_config(route_name='home', renderer='templates/mytemplate.pt')
#def my_view(request):
    #return {'project': 'Homework5'}

@view_config(route_name='index', renderer='templates/index.jinja2')
def index(request):
    return {'link': '<a href="aboutme/aboutme.html">aboutme.html</a>'}

@view_config(route_name='aboutme', renderer='templates/aboutme/aboutme.jinja2')
def aboutme(request):
    return {'link': '<a href="/">index.html</a>'}