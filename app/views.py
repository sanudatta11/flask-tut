from flask import render_template,flash, redirect
from flask import request

from app import app
from .forms import LoginForm
@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}  # fake user
    posts = [  # fake array of posts
        { 
            'author': {'nickname': 'John'}, 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': {'nickname': 'Susan'}, 
            'body': 'The Avengers movie was so cool!' 
        }
    ]
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html',
                           title='Sign In',
                           form=form,
            providers=app.config['OPENID_PROVIDERS'])

@app.route('/login2/',methods=['GET','POST'])
def login2():
    if request.method == 'GET':
        return render_template('form.html',title="Form Submit")
    elif request.method == 'POST':
        return "Username = %s and Password = %s" % (request.form['username'],request.form['password'])

@app.route('/login3/',methods=['GET','POST'])
def login3():
    return request.args.get('key','')