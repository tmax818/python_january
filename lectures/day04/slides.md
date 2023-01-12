![](../../images/coding_dojo_logo_white.png)
<!-- .slide:data-background="#000000" -->
---
# Day 4
<!-- .slide:data-background="#000000" -->
![](../../images/flask-logo.png)   <!-- .element: class="fragment" -->
---
# Overview
--
## Assignments

### Understanding Routing (Practice)
### Playground (Practice)
### Checkerboard (Core)
### HTML Table (Core)
---
# Virtual Environments
--
### `pipenv`

- Windows:
```
pip install pipenv
```
- Mac
```
pip3 install pipenv
```
This step is done ONE TIME globally.

---
# Hello Flask
--
## steps:

# We perform these steps EVERY TIME we create a new Flask app!
--
1. create a new directory for the app
--
2. create virtual environment 

```bash
pipenv install flask
```
or
```bash
python -m pipenv install flask
```
--
3. activate the virtual environment

```
pipenv shell
```
--
create `server.py`:

```py
from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
```

---
# Routes
--
```py
@app.route('/hello/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello(name):
    print(name)
    return "Hello, " + name
```
---
# Rendering Views
---
# Template Engines
---
# Static Files
---
# More Template Rendering
---
