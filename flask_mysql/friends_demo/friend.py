from mysqlconnection import connectToMySQL

class Friend:
    DB = "friends"
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.occupation = data['occupation']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


#the get_all method will be used when we neeed to retrieve all the rows of the table
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM friends;"
        results = connectToMySQL(cls.DB).query_db(query)
        friends = []
        for friend in results:
            friends.append(cls(friend))
        return friends


#the get_one method will be used when we need to retrieve just one specific row of the table
    @classmethod
    def get_one(cls, friend_id):
        query = "SELECT * FROM friend WHERE id = %(id)s;"
        data = {'id':friend_id}
        results = connectToMySQL(cls.DB).query_db(query, data) #{"id"} instead of data?
        return cls(results[0])


    @classmethod
    def save(cls, data):
        query  = """INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) 
                    VALUES ( %(first_name)s, %(last_name)s, %(occupation)s, NOW(), NOW() );"""
        #data is a dictionary that will be passed into the save method from server.py
        results = connectToMySQL(cls.DB).query_db(query, data)
        return results