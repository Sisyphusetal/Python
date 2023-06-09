from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
    DB = "dojos_and_ninjas_schema"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.ninjas = []
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(cls.DB).query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos
    
    @classmethod
    def create_dojo(cls, data):
        query = """INSERT INTO dojos(name)
            VALUES(%(name)s);"""
        results = connectToMySQL(cls.DB).query_db(query, data)
        return results
    
    @classmethod
    def get_one(cls, data):
        query = """SELECT * FROM dojos
                    WHERE id = %(dojo_id)s;"""
        results = connectToMySQL(cls.DB).query_db(query, data)
        print(results)
        return cls(results[0])\
        
    @classmethod
    def get_dojo_ninjas(cls, data):
        query = """SELECT * FROM dojos
                LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id
                WHERE dojo_id = %(dojo_id)s"""
        results = connectToMySQL(cls.DB).query_db(query, data)
        print(results)
        dojo = cls(results[0])
        for row in results:
            ninja_data = {
                "id": row["ninjas.id"],
                "first_name": row["first_name"],
                "last_name" :row["last_name"],
                "age":  row["age"],
                "created_at": row["ninjas.created_at"],
                "updated_at": row["ninjas.updated_at"]
            }
            dojo.ninjas.append(ninja.Ninja(ninja_data))
        return dojo