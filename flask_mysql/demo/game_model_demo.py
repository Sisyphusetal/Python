from mysqlconnectikon import connectToMySQL

class Game:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.genre = data['genre']
        self.release_year = data['release_year']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_all(cls):
        query = """
        SELECT * 
        FROM games;
        """

        results = connectToMySQL('games_db').query_db(query)
        
        all_games = []

        #Always pass objects to the front end when getting data from the database
        #Data reaching the front end should ALWAYS be an object
        for game in results:
            all_games.append( cls(game) )

        return all_games
    
    @classmethod
    def add_game(cls, data):
        query = """
        INSERT INTO games (name, genre, release_year)
        VALUES('Magic the Gathering', 'TCG', 1993)
        # """
        # query = """
        # INSERT INTO games (name, genre, release_year)
        # VALUES(  %(name)s, %(genre)s, %(release_year)s  )
        # """

        results = connectToMySQL(cls.DB).query_db(query, data)

        return results
    
    @classmethod
    def get_one(cls, data):
        query = """
        SELECT * 
        FROM games
        WHERE id = %(game_id)s ;
        """

        results = connectToMySQL('games_db').query_db(query, data)

        return cls(results[0])
    
    @classmethod
    def add_game(cls, data):
        query = """
        UPDATE games
        SET name = %(name)s, genre= %(genre)s, release_year = %(release_year)s
        WHERE id = %(game_id)s
        """
        # query = """
        # INSERT INTO games (name, genre, release_year)
        # VALUES(  %(name)s, %(genre)s, %(release_year)s  )
        # """

        results = connectToMySQL(cls.DB).query_db(query, data)

        return results
    
    @classmethod
    def delete_game(cls,data):
        query = """
        DELETE
        FROM games
        WHERE id = %(game_id)s ;
        
        """

        results = connectToMySQL(cls.DB).query_db(query, data)
        
        return results