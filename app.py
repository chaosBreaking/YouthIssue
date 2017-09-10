# coding: utf-8
import leancloud
import socket
import time
from flask import Flask,render_template,flash,request,url_for,redirect,session,blueprints
from flask_sockets import Sockets
from views.check import checkin,checkadmin
from sign import signHandle
from youth_keyDB import YouthDB_views

app = Flask(__name__)
# 动态路由

app.register_blueprint(YouthDB_views, url_prefix='/input')
# app.register_blueprint(todos_view, url_prefix='/todos')
# app.register_blueprint(user_return, url_prefix='/ureturn')

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('login.html')

@app.route('/sign')
def sign():
    return render_template('sign.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/LOGIN', methods=['POST'])
def LOGIN():
    fail = u'用户名或密码错误'
    name = request.form['name']
    password = request.form['password']
    if(checkin(name,password) == 'success'):
        return render_template('index.html',name=name)
    else:
        return render_template('login.html',fail=fail)

@app.route('/SIGN',methods=['POST'])
def SIGN():
    User={'name':request.form['name'],'key1': request.form['password1'],'key2': request.form['password2'],'youth_key':request.form['youth_key']}
    result = signHandle(User)
    if result == 'success':
        return render_template('index.html')
    else:
        return render_template('sign.html',state = result)


@app.route('/adminlogin', methods=['POST'])
def adminlogin():
    fail = u'用户名或密码错误'
    name = request.form['name']
    password = request.form['password']
    if(checkadmin(name,password) == 'success'):
        return redirect(url_for('input.show'))
    else:
        return render_template('admin.html',fail=fail)
