from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "Any string you want: I am the princess of Canada."       

@app.route('/')             
def hello_world():
    session['id'] = 42
    return render_template('index.html')

@app.route('/users', methods = ['POST'])
def users():
    print(request.form)
    session['name'] = request.form['name']
    session['email'] = request.form['email']
    return redirect('/')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
    

if __name__=="__main__":    
    app.run(debug=True)  