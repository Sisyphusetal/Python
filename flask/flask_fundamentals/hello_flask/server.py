from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/dojo')
def dojo():
    return 'Dojo!'


@app.route('/say/<string:name>')
def say(name):
    return f"Hi {name}!"


@app.route('/repeat/<int:num>/<string:text>')
def repeat(num,text):
    return text*num



if __name__=="__main__":
#different module
    app.run(debug=True, port=5000)