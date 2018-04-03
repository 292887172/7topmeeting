from flask import Flask,session,redirect,request

app=Flask(__name__,template_folder='templates')
app.debug = False
app.secret_key = "asdfasdf"
from .index.index import index1
from .index.mettingadd import mettingadd1
from .index.loginandlogout import loginandlogout1

@app.before_request
def process_request(*args,**kwargs):
    if request.path == '/login':
        return None
    user = session.get('user')
    if user:
        return None
    return redirect('/login')

app.register_blueprint(index1)
app.register_blueprint(mettingadd1)
app.register_blueprint(loginandlogout1)