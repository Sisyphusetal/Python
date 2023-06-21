from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    DB = "dojos_and_ninjas_schema"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
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
        return cls(results[0])