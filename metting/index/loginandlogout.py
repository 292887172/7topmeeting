import datetime
import json

from flask import Flask, request, render_template, session, redirect, Response,Blueprint
from wtforms import Form
from wtforms import validators
from wtforms import widgets
from wtforms.fields import simple
from ..db_helper import SQLHelper
class LoginForm(Form):
    user = simple.StringField(
        label='用户名',
        validators=[
            validators.DataRequired(message='用户名不能为空.'),
            validators.Length(min=2, max=18, message='用户名长度必须大于%(min)d且小于%(max)d')
        ],
        widget=widgets.TextInput(),
        render_kw={'class': 'form-control','placeholder':'用户名'}

    )
    pwd = simple.PasswordField(
        label='密码',
        validators=[
            validators.DataRequired(message='密码不能为空.'),
            validators.Length(min=8, message='用户密码长度必须大于%(min)d'),
            # validators.Regexp(regex="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{8,}",
            #                   message='密码至少8个字符，至少1个大写字母，1个小写字母，1个数字和1个特殊字符')

        ],
        widget=widgets.PasswordInput(),
        render_kw={'class': 'form-control','placeholder':'密码'}
    )

#@app.route('/login',methods=['GET','POST'],endpoint='n1')
loginandlogout1=Blueprint('loginandlogout1',__name__)
@loginandlogout1.route('/login',methods=['GET','POST'], endpoint='login')
def login():
    if request.method=='GET':
        form = LoginForm()
        return render_template('login.html',form=form)
    form = LoginForm(formdata=request.form)
    if form.validate():
        user = form.data['user']
        pwd = form.data['pwd']
        result = SQLHelper.fetch_all('Select name,id from user WHERE name=%s and pwd=%s', [user, pwd])
        if result:
            session['user'] = result[0]
            return redirect('/index')
        else:
            form.pwd.errors.append('密码错误')
            return render_template('login.html',form=form)
    else:
        return render_template('login.html',form=form)

#@app.route('/logout',methods=['GET'],endpoint='n3')
@loginandlogout1.route('/logout',methods=['GET'], endpoint='logout')
def logout():
    if request.method=='GET':
        session.pop('user', None)
        return redirect('/login')