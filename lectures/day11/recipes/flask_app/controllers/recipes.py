from flask_app import app, render_template, redirect, session, request
from flask_app.models.recipe import Recipe

@app.route('/recipes')
def recipes():
    if 'user_id' not in session:
        return redirect('/logout')
    return render_template('recipes.html')

@app.route('/recipes/new')
def new_recipe():
    return render_template('new_recipe.html')

@app.route('/recipes/create', methods = ['POST'])
def create_recipe():
    print(request.form)
    Recipe.save(request.form)
    return redirect('/recipes')
    
