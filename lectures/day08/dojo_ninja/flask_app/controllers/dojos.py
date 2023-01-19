from flask_app import app, render_template, redirect, request
from flask_app.models.dojo import Dojo

# ! CREATE
@app.route('/dojos/new')
def new_dojo():
    return render_template("new.html")

@app.route('/dojo/create', methods=["POST"])
def create_dojo():
    print(request.form)
    Dojo.save(request.form)
    return redirect('/')
    

# ! READ ALL
@app.route("/dojos")
def dojos():
    dojos = Dojo.get_all()
    print(dojos)
    return render_template("index.html", dojos = dojos)
    

# ! READ ONE
@app.route("/dojos/<int:id>")
def get_dojo(id):
    data = {'id': id}   
    return render_template('show.html', dojo = Dojo.get_one_with_ninjas(data))
    

#  ! UPDATE
@app.route("/dojos/edit/<int:id>")
def edit_dojo(id):
    data = {'id': id}   
    return render_template('edit.html', dojo = Dojo.get_one_(data))

@app.route('/dojo/update', methods=["POST"])
def update_dojo():
    Dojo.update(request.form)
    return redirect('/')

# ! DELETE        