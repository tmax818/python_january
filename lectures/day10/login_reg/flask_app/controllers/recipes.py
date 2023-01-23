from flask_app import app, render_template, session, redirect

@app.route('/recipes')
def recipes():
    if 'user_id' not in session:
        return redirect('/logout')
    return render_template('recipes.html')