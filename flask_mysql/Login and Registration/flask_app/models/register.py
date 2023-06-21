from flask_app.config.mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt
import re

bcrypt = Bcrypt(app)

class Register:
    DB = "login_and_registration_schema"
    def __init__(cls, data):
        self.id = data['id']