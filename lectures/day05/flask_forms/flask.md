
# FLASK

### [Virtual Environments](https://login.codingdojo.com/m/172/7219/54533)

## install `pipenv`
**You only do this once!!!**

windows:
```bash
pip install pipenv
```
mac:
```bash
pip3 install pipenv
```
## Creating a virtual environment with `pipenv` & installing flask
**You do this EVERY TIME!!! YES, EVERY TIME!!**
- First, create a new folder for the project

```bash
mkdir hello_flask
cd hello_flask
```
`mkdir hello_flask` is the cli command to create a folder/directory called 'hello_flask'. `cd hello_flask` is the cli command to move into the folder called 'hello_flask'. You need to be *inside* the folder before following the next steps. The folder you create for each project CANNOT BE INSIDE ANOTHER FLASK PROJECT FOLDER!!! 

- create the virtual environment.

windows:
```bash
python -m pipenv install flask
```
mac:
```bash
python3 -m pipenv install flask
```

## Activating the virtual environment

```bash
pipenv shell
```

## Create the `server.py` file for our project: [Hello Flask](https://login.codingdojo.com/m/172/7219/52126)

```py
from flask import Flask     # Import Flask to allow us to create our app
app = Flask(__name__)       # Create a new instance of the Flask class called "app"

@app.route('/')             # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'   # Return the string 'Hello World!' as a response

if __name__=="__main__":    # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)     # Run the app in debug mode.
```

ALWAYS name this file: `server.py`

## Running the server file

windows:
```bash
python server.py
```
mac:
```bash
python3 server.py
```

# [Routing](https://login.codingdojo.com/m/172/7219/52127)

## Http Request/Response cycle

- When we visit [google](https://www.google.com/) or [localhost](http://localhost:5000/) we send a GET request to the server at that address.

```py
@app.route('/')            
def hello_world():
    return 'Hello World!'
```

## Using decorator to listen for end points

The English translation of the above Python code in the context of Flask is something like this, "Hey web server! Pay attention! If you see someone type: http://localhost:5000/ into their web browser, send them the string 'Hello World!'"

The same is true for the following:

```py
@app.route('/success')
def success():
    return "success"
```
"Hey web server! Pay attention! If you see someone type: http://localhost:5000/success into their web browser, send them the string 'success'. You got it!"

## Attaching functions to the decorators

```py
@app.route('/success')
```
is a decorator. It 'decorates' whatever function comes after it. So adding the function

```py
def success():
    return "success"
```
after the decorator, tells Flask to invoke the Python function `success`.

# [Rending Templates](https://login.codingdojo.com/m/172/7219/52129)

## Rendering a template html

- We want to build web apps not return cute strings! To return HTML files instead of strings, we need the `render_template` method built into Flask. 

- to use a method in Python we either write the method ourselves, or import a method someone else wrote. We import the `render_template` method on the first line of [server.py](server.py) 

```py
from flask import Flask, render_template  # added render_template!
```

- once we import the method, we can use it!

```py
@app.route('/')                           
def hello_world():
    return render_template('index.html')
```

- The first argument passed to `render_template` is the string version of the name of the HTML file we want to render. All HTML files we want to render in our application have to be in a directory called [templates](./templates/index.html). Make sure you spell the name of the file correctly!

## [Jinja 2](https://login.codingdojo.com/m/172/7219/52130)

[Jinja 2](https://palletsprojects.com/p/jinja/) is the template engine for Flask. Be sure to add the [extension](https://marketplace.visualstudio.com/items?itemName=WyattFerguson.jinja2-snippet-kit) to VScode.

## Passing data from server to template

- The `render_template` function takes additional arguments. Any data we want to pass from the backend to our templates can be passed as additional arguments to the `render_template` function.

```py
@app.route('/')             
def hello_world():
    fruits = ['straberry', 'banana', 'kiwi']
    return render_template("index.html", fruits = fruits)  
```

- The `fruits` variable will now be available in our Jinja templates.


## Looping with Jinja & displaying information

- We can access the list stored in the `fruit` variable using Jinja

```html
    <ul>
    {% for fruit in fruits %}
        <li>{{fruit}}</li>
        {% endfor %}
    </ul>
```

# Path Variables

## 4 ways
|interpolation | file |
|---|---|
|`f"My name is {name}"`| inside a `.py` file|
|`@app.route('/about/<name>/<int:num>')`| inside a `.py` file only inside `@app.route`|
|`<h1>{{name}}</h1>`|only in `.html`|
|||
## Setting up routes to accept path variables

## Sending variables from browser

## Conversion of path variables into data types

# Static Files
## Setting up css, img, and js files

## Linking the static files into templates

# Post Form Submission


