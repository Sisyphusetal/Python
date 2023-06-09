from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_bcrypt import Bcrypt


bcrypt = Bcrypt(app)


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

    login_data = {'email': request.form['email']}
    user_in_db = User.get_user_by_email(login_data)

    if not user_in_db:
        flash('Invalid email/password')
        return redirect('/')
    
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash('Invalid email/password')
        return redirect('/')
    
    session['user_id'] = user_in_db.id

    return redirect(f'/welcome/{ user_in_db.id }')

@app.route('/user_register', methods=['POST'])
def user_register():
    if not User.validate_user_registration(request.form):
        return redirect('/')
    
    pw_hash = bcrypt.generate_password_hash(request.form['password'])

    newUser_data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': pw_hash
    }

    user_id = User.create_new_user(newUser_data)
    session['user_id'] = user_id

    return redirect(f'/welcome/{user_id}')



@app.route('/register/<int:user_id>')
def register_page():
    return render_template('welcome.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')