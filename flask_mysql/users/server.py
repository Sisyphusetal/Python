from flask import Flask, render_template, request, redirect, session

from users import User
app = Flask(__name__)


@app.route('/')
def index():
    all_users = User.get_all()
    print(all_users)
    return render_template('read_all.html', users=all_users)

@app.route('/selected_user/<int:user_id>')
def single_user(user_id):
    data = {"user_id": user_id}
    user = User.get_one(data)
    return render_template('single_user.html', user=user)

@app.route('/edit_user/<int:user_id>')
def edit_user(user_id):
    data = {"user_id": user_id}
    user = User.get_one(data)
    return render_template('edit_user.html', user=user)

@app.route('/create')
def new_user():
    return render_template('create.html')

@app.route('/create_user', methods=['POST'])
def create_user():
    newID = User.save(request.form)
    return redirect(f'/selected_user/{newID}')

@app.route('/update_user/<int:user_id>', methods=['POST'])
def update_user(user_id):
    data = {"user_id": user_id, "first_name": request.form['first_name'],
            "last_name": request.form['last_name'], "email": request.form['email']}
    User.update_user(data)
    return redirect(f'/selected_user/{user_id}')

@app.route('/delete_user/<int:user_id>')
def delete_user(user_id):
    data = {"user_id": user_id}
    User.delete_user(data)
    return redirect('/')







if __name__ == "__main__":
    app.run(debug=True)