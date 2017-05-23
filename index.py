#!/usr/bin/env python
# -*- coding:utf-8 -*-

from bottle import route,run,template,error

@route('/')
def index():
    return template('hoge') # viewsディレクトリ配下にhoge.tpl hoge.htmlがあった場合はhoge.tplが優先される

@route('/api/<id>')
def api(id):
    return template('hoge',id=id)

@error(404)
def error404(error):
    return template('404')

run(host='0.0.0.0', port=80, debug=True, reloader=True)
