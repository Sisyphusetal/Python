from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "Wood 5"

@app.route('/')
def default():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/result')


@app.route('/result')
def result():
    return render_template('results.html')


@app.route('/refresh')
def refresh():
    session.clear()
    return redirect('/')









if __name__=="__main__":
#different module
    app.run(debug=True)