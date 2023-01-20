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
    User.save(request.form) # THIS WILL NOT WORK!!!
    # TODO log in the user

    # TODO redirect user to app
    return redirect('/things')


#! READ and VERIFY AKA LOGIN

@app.route('/login', methods=['post'])
def login():
    # TODO see of the email is in our DB
    # TODO check to see of the password provided matches the password in our DB
    # TODO log in the user
    
    # TODO redirect user to app
    return redirect('/things')
    
    


#! LOGOUT

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

