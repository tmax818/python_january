from flask_app import app, render_template, redirect, session, request
from flask_app.models.recipe import Recipe

@app.route('/recipes')
def recipes():
    if 'user_id' not in session:
        return redirect('/logout')
    return render_template('recipes.html', recipes = Recipe.get_all())

@app.route('/recipes/new')
def new_recipe():
    return render_template('new_recipe.html')

@app.route('/recipes/create', methods = ['POST'])
def create_recipe():
    print(request.form)
    if not Recipe.validate_recipe(request.form):
        return redirect('/recipes/new')
    Recipe.save(request.form)
    return redirect('/recipes')

@app.route('/recipes/<int:id>')
def show_recipe(id):
    data = {'id': id}
    return render_template("show_recipe.html", recipe = Recipe.get_one(data))

@app.route("/recipes/edit/<int:id>")
def edit_recipe(id):
    data = {'id': id}
    return render_template("edit_recipe.html", recipe = Recipe.get_one(data))
    
@app.route('/recipes/update', methods = ["POST"])
def update_recipe():
    print(request.form)
    if not Recipe.validate_recipe(request.form):
        return redirect(f"/recipes/edit/{request.form['id']}")
    Recipe.update(request.form)
    return redirect('/recipes') 
