from flask import Flask render_template, redirect,
#Importing the class from friend.py
from friend import Friend
app = Flask(__name__)

@app.route('/')
def index():
    #call the class method to get all friends
    friends = Friend get_all()
    print(friends)
    return render_template('index.html', friend=friends)






if __name__ == __main__:
    app.run(debug=True)


# %(key_name)s