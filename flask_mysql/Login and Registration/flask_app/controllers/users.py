from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User




@app.route('/')
def index():
    return render_template('index.html')

@app.route('/welcome/<int:user_id>')
def welcome(user_id):
    
    if 'user_id' not in session:
        return redirect('/')
    
    user = User.get_user_by_id({'user_id': user_id})

    return render_template('welcome.html', user=user)

@app.route('/user_login', methods=['POST'])
def user_login():

    return redirect(f'/welcome/')

@app.route('/user_register', methods=['POST'])
def user_register():
    if not User.validate_user_registration(request.form):
        return redirect('/')
    
    user_id = User.create_new_user(request.form)
    session['user_id'] = user_id

    return redirect(f'/welcome/{user_id}')



@app.route('/register/<int:user_id>')
def register_page():
    return render_template('welcome.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')