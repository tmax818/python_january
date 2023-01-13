from flask import Flask, render_template, redirect  
from users import users   
app = Flask(__name__)       

@app.route('/')
def index():
    return render_template("index.html", users = users)

@app.route('/about/<something>')
def about(something):
    return render_template('about.html', something = something)

@app.route('/logout')
def logout():
    return redirect('/')
          

if __name__=="__main__":    
    app.run(debug=True)     