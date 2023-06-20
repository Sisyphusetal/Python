from flask import Flask, render_template, request, redirect, session

from users import User
app = Flask(__name__)


@app.route('/')
def index():
    all_users = User.get_all()
    print(all_users)
    return render_template('read_all.html', users=all_users)

@app.route('/create')
def new_user():
    return render_template('create.html')

@app.route('/create_user', methods=['POST'])
def create_user():
    User.save(request.form)
    return redirect('/')






if __name__ == "__main__":
    app.run(debug=True)