from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo


@app.route('/')
def index():
    all_dojos = Dojo.get_all()
    print(all_dojos)
    return render_template("dojos.html", dojos=all_dojos)


@app.route('/create_dojo', methods=['POST'])
def create_dojo():
    print(request.form)
    Dojo.create_dojo(request.form)
    return redirect('/')

@app.route('/dojos/<int:dojo_id>')
def show_dojo(dojo_id):
    data = {'dojo_id': dojo_id}
    dojo = Dojo.get_dojo_ninjas(data)
    return render_template('selected_dojo.html', dojo=dojo)

@app.route('/create_ninja', methods=['POST'])
def create_ninja():
    print(request.form)
    Ninja.new_ninja(request.form)

    return redirect(f'/dojos/{request.form["dojo_id"]}')

@app.route('/create_ninja_form')
def ninja_form():
    dojos = Dojo.get_all()
    return render_template('ninjas.html', dojos=dojos)
