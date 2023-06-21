from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.login import Login
from flask_app.models.register import Register


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')