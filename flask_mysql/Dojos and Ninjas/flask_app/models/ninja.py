from flask_app.config.mysqlconnection import connectToMySQL


class Ninja:
    DB = "dojos_and_ninjas_schema"
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas"
        results = connectToMySQL(cls.DB).query_db(query)
        ninjas = []
        for ninja in results:
            ninjas.append(cls(ninja))
        return ninjas
    
    @classmethod
    def get_dojo_ninjas(cls, data):
        query = """SELECT * FROM ninjas
                WHERE dojo_id = %(dojo_id)s"""
        results = connectToMySQL(cls.DB).query_db(query, data)
        print(results)
        return results