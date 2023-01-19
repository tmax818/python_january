from flask_app.config.mysqlconnection import connectToMySQL
from pprint import pprint


DATABASE = 'users_cr'

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # ! CREATE
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s,%(last_name)s, %(email)s);"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    #  ! READ ALL
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(DATABASE).query_db(query)
        pprint(results)
        users = []
        for user in results:
            users.append( User(user) )
        return users
    
    # ! READ ONE
    
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query,data)
        pprint(result[0])
        user = User(result[0])
        print(user)
        return user
        
    
    #  ! UPDATE
    
    @classmethod
    def update(cls, data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)
    
    # ! DELETE