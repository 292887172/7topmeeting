from flask import Flask,request,render_template,session,redirect,Response
from db_helper import SQLHelper
import json
import datetime
from wtforms import Form
from wtforms.fields import core
from wtforms.fields import html5
from wtforms.fields import simple
from wtforms import validators
from wtforms import widgets

app=Flask(__name__,template_folder='templates')
app.debug = True
app.secret_key = "asdfasdf"

@app.before_request
def process_request(*args,**kwargs):
    if request.path == '/login':
        return None
    user = session.get('user')
    if user:
        return None
    return redirect('/login')

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

@app.route('/login',methods=['GET','POST'],endpoint='n1')
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

@app.route('/index',methods=['GET','POST'],endpoint='n2')
def index():
    time = SQLHelper.fetch_all('Select id,datetime from time ', [])
    room = SQLHelper.fetch_all('Select id,name from room ', [])
    user = session.get('user')[0]
    if request.method=='GET':
        dt=datetime.datetime.today().strftime('%Y/%m/%d')
        reseve_list = SQLHelper.fetch_all('Select rid,tid,name from reseve  INNER JOIN user ON reseve.uid=user.id WHERE reseve.date=%s', [dt])
        reseve_dict = {}
        for item in reseve_list:
            if reseve_dict.get(item[0]):
                reseve_dict[item[0]]['time'][item[1]]=item[2]
            else:
                reseve_dict[item[0]] = {'time': {item[1]:item[2]}}
        return render_template('index.html',time_list=time,room_list=room,user=user,reseve_dict=reseve_dict,dt=dt)
    else:

        date=request.form.get('datetime')
        if date:
            dt=datetime.date(*map(int, date.split('/')))
            reseve_list=SQLHelper.fetch_all('Select rid,tid,name from reseve  INNER JOIN user ON reseve.uid=user.id WHERE reseve.date=%s', [dt])
            reseve_dict={}
            for item in reseve_list:
                if reseve_dict.get(item[0]):
                    reseve_dict[item[0]]['time'][item[1]] = item[2]
                else:
                    reseve_dict[item[0]] = {'time': {item[1]: item[2]}}
            return render_template('index.html',time_list=time,room_list=room,user=user,reseve_dict=reseve_dict,dt=date)
        else:
            return redirect('/index')

@app.route('/logout',methods=['GET'],endpoint='n3')
def logout():
    if request.method=='GET':
        session.pop('user', None)
        return redirect('/login')
@app.route('/add',methods=['POST'],endpoint='n4')
def add():
    if request.method=='POST':
        rid=request.form.get('rid')
        tid = request.form.get('tid')
        date=request.form.get('date')
        uid=session.get('user')[1]
        user=session.get('user')[0]
        row=SQLHelper.add('INSERT INTO reseve(rid, date, tid,uid) VALUES (%s, %s, %s,%s)',[rid,date,tid,uid])
        ret={'stude':row,'user':user}
        return Response(json.dumps(ret))

if __name__== '__main__':
    app.run()

