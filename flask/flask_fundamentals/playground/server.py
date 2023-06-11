from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return "Default page go brrr"

@app.route('/play')
def play():
    return render_template('index.html', boxes = 3, color = 'blue')

@app.route('/play/<int:x>')
def playNumber(x):
    return render_template('index.html', boxes = x, color = 'blue')

@app.route('/play/<int:x>/<color>')
def playNumberColor(x, color):
    return render_template('index.html', boxes = x, color = color)



if __name__=="__main__":
#different module
    app.run(debug=True, port=5000)