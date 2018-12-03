from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm, CameraForm, RcontrolForm
import numpy as np

import videocontrol as rc

#rc.webControl('10','10')
def saveFunc(a):
    
    fo = open("foo.txt", "wb")
    fo.write(a);
    fo.close()
    

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Foad'}
    posts = [
        {
            'author': {'nickname': 'UMASH'},
            'body': 'Perfect !'
        },
        {
            'author': {'nickname': 'UTeh'},
            'body': 'Problems!'
        }
    ]
    return render_template('index.html',
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


@app.route('/liveview', methods=['GET', 'POST'])
def liveview():
    form = SyringeForm()
    if form.validate_on_submit():
        flash('Syringe Down="%s", Plunger Pull=%s' %
              (form.syringe.data, form.plunger.data))
    
        return redirect('/index')
    return render_template('liveview.html',
                           title='Live View',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])





@app.route('/remotecontrol', methods=['GET', 'POST'])
def remotecontrol():
    form = RcontrolForm()
    if form.validate_on_submit():
        flash('Experiment="%s", Runs=%s' %
              (form.experiment.data, form.runs.data))
        saveFunc(form.experiment.data)
        #rc.webControl(form.experiment.data,form.runs.data)
        #rc.webControl('10','10')
        return redirect('/index')
    return render_template('remotecontrol.html',
                           title='Remote Control',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])
