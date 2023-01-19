from flask_app.config.mysqlconnection import connectToMySQL
from pprint import pprint


DATABASE = 'dojos_and_ninjas_schema'

class Ninja:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojo_id = data['dojo_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    # ! CREATE
    @classmethod
    def save(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age) VALUES (%(first_name)s,%(last_name)s, %(age)s);"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    #  ! READ ALL
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL(DATABASE).query_db(query)
        pprint(results)
        ninjas = []
        for ninja in results:
            ninjas.append( Ninja(ninja) )
        return ninjas
    
    # ! READ ONE
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM ninjas WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query,data)
        pprint(result[0])
        ninja = Ninja(result[0])
        print(ninja)
        return ninja
        
    #  ! UPDATE
    @classmethod
    def update(cls, data):
        query = "UPDATE ninjas SET first_name = %(first_name)s, last_name = %(last_name)s, age = %(age)s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)
    
    # ! DELETE