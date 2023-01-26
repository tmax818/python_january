from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import flash
from pprint import pprint
DATABASE = 'recipes'

class Recipe:
    
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_made = data['date_made']
        self.under_30 = data['under_30']
        self.user_id = data['user_id']
        self.number_served = data['number_served']
        self.first_name = data['first_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def save(cls, data):
        query = "INSERT INTO recipes (name, description, instructions, date_made, under_30, number_served, user_id) VALUES (%(name)s, %(description)s, %(instructions)s, %(date_made)s, %(under_30)s, %(number_served)s, %(user_id)s)"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes JOIN users ON users.id = recipes.user_id;"
        results = connectToMySQL(DATABASE).query_db(query)
        pprint(results)
        recipes = []
        for recipe in results:
            recipes.append(cls(recipe))
        return recipes
    
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM recipes JOIN users ON users.id = recipes.user_id WHERE recipes.id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        print(result[0])
        return Recipe(result[0])
    
    @classmethod
    def update(cls, data):
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, date_made = %(date_made)s, under_30 = %(under_30)s, number_served = %(number_served)s WHERE recipes.id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)
        
    @staticmethod
    def validate_recipe(recipe):
        is_valid = True
        if len(recipe['name']) < 3:
            flash("Name must be three chars")
            is_valid = False
        if len(recipe['description']) < 3:
            flash("Desc must be three chars")
            is_valid = False
        if len(recipe['instructions']) < 3:
            flash("INst must be three chars")
            is_valid = False
        if not 'under_30' in recipe:
            flash("must select option for under 30 min.")
            is_valid = False
        if recipe['date_made'] == '':
            flash("Please select a date")
            is_valid = False
        if int(recipe['number_served']) <= 0:
            flash("Recipe has to serve at least 1 person")
            is_valid = False
        return is_valid