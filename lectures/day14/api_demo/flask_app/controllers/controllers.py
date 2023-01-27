from flask_app import app, render_template, base_url, pprint, requests, redirect, request, jsonify

@app.route('/')
def index():
    data = requests.get(base_url).json()
    return render_template('index.html', data = data)

# @app.route('/<topic>')
# def display_topic(topic):
#     data = requests.get(base_url + topic).json()
#     return render_template('index.html', data = data)

@app.route('/character')
def display_topic():
    data = requests.get(base_url + 'character').json()
    return render_template('index.html', data = data)
    
@app.route('/location')
def display_loc():
    data = requests.get(base_url + 'location').json()
    return render_template('index.html', data = data)

@app.route('/search', methods = ['POST'])
def search():
    print(request.form)
    req = f"https://rickandmortyapi.com/api/character/?name={request.form['q']}"
    data = requests.get(req).json()
    return render_template('index.html', data=data)

@app.route('/api')
def api():
    data = [
    {'name': 'Tyler', 'age': 39},
    {'name': 'Eric', 'age': 22}
        
    ]
    return jsonify(data)
    
    
    