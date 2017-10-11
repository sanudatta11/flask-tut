from flask import render_template,flash, redirect
from flask import request
from flask import session
from flask import url_for
from werkzeug.utils import secure_filename, escape
from flask_mysqldb import MySQL
from flask import Flask
from connect import connect_mysql

from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    if 'username' in session:
        user = {'nickname': escape(session['username']) }

    user = {'nickname': "No user"}

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

@app.route('/upload/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/media/sanu/med/upload/' + secure_filename(f.filename))
    return "Done"


# For Session Check
@app.route('/logsess',methods=['GET','POST'])
def login4():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
            <form method="post">
                <p><input type=text name=username>
                <p><input type=submit value=Login>
            </form>
        '''
@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/update')
def update():
    try:
        retr = connect_mysql()
        if retr == 1:
            return "Update Done"
        else:
            return "Update Failed! Rollbacked"
    except:
        return '''
                Couldn't Fetch
                '''

# set the secret key.  keep this really secret:
app.secret_key = str('A0Zr98j/3yX R~XHH!jmN]LWX/,?RT')