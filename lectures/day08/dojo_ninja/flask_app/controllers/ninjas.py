from flask_app import app, render_template, redirect, request
from flask_app.models.ninja import Ninja

# ! CREATE
@app.route('/ninjas/new')
def new_ninja():
    return render_template("new.html")

@app.route('/ninja/create', methods=["POST"])
def create_ninja():
    print(request.form)
    Ninja.save(request.form)
    return redirect('/')
    

# ! READ ALL
@app.route("/")
def ninjas():
    return render_template("index.html", ninjas = Ninja.get_all())
    

# ! READ ONE
@app.route("/ninjas/<int:id>")
def get_ninja(id):
    data = {'id': id}   
    return render_template('show.html', ninja = Ninja.get_one(data))
    

#  ! UPDATE
@app.route("/ninjas/edit/<int:id>")
def edit_ninja(id):
    data = {'id': id}   
    return render_template('edit.html', ninja = Ninja.get_one(data))

@app.route('/ninja/update', methods=["POST"])
def update_ninja():
    Ninja.update(request.form)
    return redirect('/')

# ! DELETE        