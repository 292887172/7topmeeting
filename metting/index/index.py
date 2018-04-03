import datetime
import json

from flask import Flask, request, render_template, session, redirect, Response,Blueprint
from wtforms import Form
from wtforms import validators
from wtforms import widgets
from wtforms.fields import simple

from metting.db_helper import SQLHelper
#@app.route('/index',methods=['GET','POST'],endpoint='n2')
index1=Blueprint('index',__name__)
@index1.route('/index',methods=['GET','POST'], endpoint='index')
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
