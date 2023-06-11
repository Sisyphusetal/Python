from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def default():
    return 'default page go brr'


users = [
    {'first_name' : 'Michael', 'last_name' : 'Choi'},
    {'first_name' : 'John', 'last_name' : 'Supsupin'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

@app.route('/table')
def userTable():
    return render_template('index.html', users=users)



if __name__=="__main__":
#different module
    app.run(debug=True, port=5000)
