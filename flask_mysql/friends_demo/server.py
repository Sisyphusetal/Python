from flask import Flask, render_template, request, redirect, session
#Importing the class from friend.py
from friend import Friend
app = Flask(__name__)

@app.route('/')
def index():
    #call the class method to get all friends
    friends = Friend.get_all()
    print(friends)
    return render_template('index.html', friend=friends)

@app.route('/create_friend', methods=["POST"])
def create_friend():
    Friend.save(request.form)
    
    #First we make a data dictionary from our request.form coming from our template
    # the keys in data need to line up exactly with the variables in our query string
    # data = {
    #     "fname": request.form["fname"],
    #     "lname": request.form["lname"],
    #     "occ": request.form["occ"]
    # }
    #we pass the data dictionary into the save method from the Friend class
    # Friend.save(data)
    #Don't forget to redirect after saving to the database

    return redirect('/')


@app.route('/friend/show/<int:friend_id>')
def show(friend_id):
    #calling the get_one method and supplying it with the id of the friend we want to get
    friend = Friend.get_one(friend_id)
    return render_template("show_friend.html", friend=friend)






if __name__ == "__main__":
    app.run(debug=True)


# %(key_name)s