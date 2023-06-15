from flask import Flask, render_template, request, redirect, session
app=Flask(__name__)
app.secret_key = "Wood 5"

from game_model import Games

@app.route('/')
def Home():

    all_games = Games.get_all()
    print(all_games)
    return render_template('index.html', all_games = all_games)


@app.route('/game_form')
def show_form():
    return render_template('game_form.html')



@app.route('/submit_game_form', methods=['POST'])
def submit_game_form():
    data = {
        'name' : request.form['name'],
        'genre' : request.form['genre'],
        'release_year' : request.form['release_year']
    }
    return redirect('/')

@app.route('/edit/<int:game_id')
def show_edit_form(game_id):
    
    one_game = Games.get_one({{'game_id': game_id}})

    return render_template('/edit_form.html', one_game = one_game)

@app.route('/edit_game', methods=['POST'])
def edit_game():

    print(request.form)

    Games.update_game(request.form)


@app.route('/delete/<int:game.id>')
def delete_game(game_id):

    Games.delete_game( {'game_id' : game_id})
    return redirect('/')
