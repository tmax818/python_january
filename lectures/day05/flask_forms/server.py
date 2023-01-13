from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "Any string you want: I am the princess of Canada."       

@app.route('/')             
def hello_world():
    return render_template('index.html')

@app.route('/users', methods = ['POST'])
def users():
    print(request.form['lucky'])
    session['lucky'] = request.form['lucky']
    session['tyler'] = request.form['tyler']
    return redirect('/')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
    

if __name__=="__main__":    
    app.run(debug=True)  