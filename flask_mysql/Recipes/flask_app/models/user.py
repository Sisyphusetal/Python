from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask_bcrypt import Bcrypt
from flask import flash
import re
from flask_app.models import recipe

bcrypt = Bcrypt(app)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    DB = "recipes_schema"
    
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']

    @classmethod
    def create_new_user(cls,data):
        query = """INSERT INTO users (first_name, last_name, email, password) 
        VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"""
        return connectToMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def get_user_by_email(cls, data):
        query = """SELECT * FROM users
                WHERE email = %(email)s;"""
        result = connectToMySQL(cls.DB).query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])
    
    @classmethod
    def get_user_by_id(cls, data):
        query = """SELECT * FROM users
                WHERE id = %(user_id)s;"""
        result = connectToMySQL(cls.DB).query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])
    

    # user = dojo, ninja = recipe
    @classmethod
    def get_user_recipes(cls, data):
        query = """SELECT * FROM users
                LEFT JOIN recipes ON recipes.user_id = user.id
                WHERE user_id = %(user_id)s"""
        results = connectToMySQL(cls.DB).query_db(query, data)
        print(results)
        user = cls(results[0])
        for row in results:
            recipe_data = {
                "id": row["recipes.id"],
                "name": row["name"],
                "description": row["description"],
                "instructions":  row["instructions"],
                "date_made":  row["date_made"],
                "under_30":  row["under_30"],
                "created_at": row["recipes.created_at"],
                "updated_at": row["recipes.updated_at"]
            }
            user.recipes.append(recipe.Recipe(recipe_data))
        return user


    @staticmethod
    def validate_user_email(user_email):
        is_valid = True
        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(user_email['email']): 
            flash("Invalid email address!")
            is_valid = False
        return is_valid
    
    @staticmethod
    def validate_user_registration(new_user):
        is_valid = True # we assume this is true
        if User.get_user_by_email(new_user):
            flash("User already exists.")
            is_valid = False
        if len(new_user['first_name']) < 3:
            flash("First name must be at least 2 characters.")
            is_valid = False
        if len(new_user['last_name']) < 3:
            flash("Last name must be at least 2 characters.")
            is_valid = False
        if not EMAIL_REGEX.match(new_user['email']): 
            flash("Please enter a valid email.")
            is_valid = False
        if len(new_user['password']) < 8:
            flash("Password must be at least 8 characters long.")
            is_valid = False
        if new_user['password'] != new_user['confirm_password']:
            flash("Password confirmation did not match.")
            is_valid = False
        return is_valid
