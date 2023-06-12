from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'Wood 5'

@app.route('/')
def default():
    session['counter'] = session.get('counter', 0) + 1
    return render_template('index.html', counter=session['counter'])

@app.route('/plus_two', methods=['POST'])
def plusTwo():
    session['counter'] = session.get('counter', 0) + 1
    return redirect('/')

@app.route('/destroy_session', methods=['POST'])
def endSession():
    session.clear()
    return redirect('/')


if __name__=="__main__":
#different module
    app.run(debug=True, port=5000)


