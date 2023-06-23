from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash

class Recipe:
    DB = 'recipes_schema'

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_made = data['date_made']
        self.under_30 = data['under_30']

    @classmethod
    def create_recipe(cls, data):
        query = """INSERT INTO recipes (name, description, instructions, date_made, under_30) 
            VALUES (%(name)s, %(description)s, %(instructions)s, %(date_made)s, %(under_30)s);"""
        return connectToMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def edit_recipe(cls, data):
        query = """UPDATE recipes
                SET name=%(name)s, description=%(description)s, instructions=%(instructions)s, date_made=%(date_made)s, under_30=%(under_30)s
                WHERE id = %(recipe_id)s;"""
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def delete_recipe(cls,data):
        query = """DELETE FROM recipes
                WHERE id = %(recipe_id)s;"""
        return connectToMySQL(cls.DB).query_db(query, data)