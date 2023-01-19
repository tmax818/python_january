from flask_app import app, render_template, redirect, request
from flask_app.models.user import User
# ! CREATE

@app.route('/users/new')
def new_user():
    return render_template("new.html")

@app.route('/user/create', methods=["POST"])
def create_user():
    print(request.form)
    User.save(request.form)
    return redirect('/')
    

# ! READ ALL
@app.route("/")
def index():
    return render_template("index.html", users = User.get_all())
    

# ! READ ONE

@app.route("/users/<int:id>")
def get_user(id):
    data = {'id': id}
    
    return render_template('show.html', user = User.get_one(data))
    

#  ! UPDATE

@app.route("/users/edit/<int:id>")
def edit(id):
    data = {'id': id}   
    return render_template('edit.html', user = User.get_one(data))

@app.route('/user/update', methods=["POST"])
def update():
    User.update(request.form)
    return redirect('/')

# ! DELETE        