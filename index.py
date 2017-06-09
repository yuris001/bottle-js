#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
from bottle import route,run,template,error, static_file, TEMPLATE_PATH

@route('/')
def index():
    return template('hoge') # viewsディレクトリ配下にhoge.tpl hoge.htmlがあった場合はhoge.tplが優先される

@error(404)
def error404(error):
    return template('404')

# index.pyが設置されているディレクトリの絶対パスを取得
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# テンプレートファイルを設置するディレクトリのパスを指定
TEMPLATE_PATH.append(BASE_DIR + "/views")
 
@route('/css/<filename>')
def css_dir(filename):
    """ set css dir """
    return static_file(filename, root=BASE_DIR+"/static/css")
 
@route('/js/<filename>')
def js_dir(filename):
    """ set js dir """
    return static_file(filename, root=BASE_DIR+"/static/js")

#@route('/css/<filename>')
#def css_static(filename):
#    return static_file(filename, root='./css')
#
#@route('/js/<filename>')
#def js_static(filename):
#    return static_file(filename, root='./js')

run(host='0.0.0.0', port=80, debug=True, reloader=True)
