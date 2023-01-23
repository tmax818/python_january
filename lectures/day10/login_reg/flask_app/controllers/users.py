from flask_app import app, render_template, redirect, request, bcrypt, session, flash
from flask_app.models.user import User

@app.route('/')
def index():
    return render_template('index.html')

#! CREATE AKA REGISTER

@app.route("/register", methods = ['post'])
def register():
    print(request.form)

    # TODO validate our user
    if not User.validate_user(request.form):
        return redirect('/')
    # TODO hash the password
    hashed_pw = bcrypt.generate_password_hash(request.form['password'])
    print(hashed_pw)
    # TODO save the user to the database
    user_data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': hashed_pw
    }
    user_id = User.save(user_data)
    # TODO log in the user
    session['user_id'] = user_id
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    # TODO redirect user to app
    return redirect('/recipes')


#! READ and VERIFY AKA LOGIN

@app.route('/login', methods=['post'])
def login():
    print(request.form)
    # TODO see if the email is in our DB
    user = User.get_by_email(request.form)
    if not user:
        flash("invalid credentials")
        return redirect("/")
    # TODO check to see of the password provided matches the password in our DB
    password_valid = bcrypt.check_password_hash(user.password, request.form['password'])
    print(password_valid)
    if not password_valid:
        flash("invalid credentials")
        return redirect('/')
    # TODO log in the user
    session['user_id'] = user.id
    session['first_name'] = user.first_name
    session['last_name'] = user.last_name
    # TODO redirect user to app
    return redirect('/recipes')
    
    


#! LOGOUT

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

