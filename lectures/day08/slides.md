![](../../images/coding_dojo_logo_white.png)
<!-- .slide:data-background="#000000" -->

---
<!-- .slide:data-background="#000000" -->
# database connection
---
## overview
--
![](../../images/flask-logo.png)
<!-- .element: class="fragment" -->
![](../../images/mysql.png)
<!-- .element: class="fragment" -->
--

## Connection to a database starts with three files
1. `server.py`   <!-- .element: class="fragment" -->
2. `mysqlconnection.py`   <!-- .element: class="fragment" -->
3. `model.py`   <!-- .element: class="fragment" -->
---
## MySQL Workbench review
---
<!-- .slide:data-background="#000000" -->
## connecting to a database
--
<!-- .slide:data-background="#000000" -->
### `mysqlconnection.py`
```py
## mysqlconnection.py

import pymysql.cursors
class MySQLConnection:
    def __init__(self, db):
        connection = pymysql.connect(host = 'localhost',
        user = 'root',
        password = 'root', 
        db = db,
        charset = 'utf8mb4',
        cursorclass = pymysql.cursors.DictCursor,
        autocommit = True)
        self.connection = connection
## Continued...
```
--
<!-- .slide:data-background="#000000" -->
```py

## mysqlconnection.py

    def query_db(self, query, data=None):
        with self.connection.cursor() as cursor:
            try:
                query = cursor.mogrify(query, data)
                print("Running Query:", query)
                executable = cursor.execute(query, data)
                if query.lower().find("insert") >= 0:
                    self.connection.commit()
                    return cursor.lastrowid
                elif query.lower().find("select") >= 0:
                    result = cursor.fetchall()
                    return result
                else:
                    self.connection.commit()
            except Exception as e:
                print("Something went wrong", e)
                return False
            finally:
                self.connection.close() 
## continued...
```
<!-- .element: class="r-stretch" -->
--
```py

## mysqlconnection.py

def connectToMySQL(db):
    return MySQLConnection(db)
```
<!-- .element: class="r-fit" -->
<!-- .slide:data-background="#000000" -->
--
<!-- .element: class="r-fit" -->
<!-- .slide:data-background="#000000" -->
### `friend.py`

```py
from mysqlconnection import connectToMySQL

class Friend:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.occupation = data['occupation']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM friends;"
        results = connectToMySQL('first_flask').query_db(query)
        friends = []
        for friend in results:
            friends.append( cls(friend) )
        return friends
```
<!-- .element: class="r-stretch" -->
--
<!-- .slide:data-background="#000000" -->
### `server.py`
```py
from flask import Flask, render_template
from friend import Friend
app = Flask(__name__)

@app.route("/")
def index():
    friends = Friend.get_all()
    print(friends)
    return render_template("index.html")
            
if __name__ == "__main__":
    app.run(debug=True)

```

            
---
## mysql connection errors (optional)
--
I don't know, man...
---
# CRUD
---
## retrieving and displaying data
--
# C
# R<!-- .element: class="fragment highlight-red" -->
# U
# D
--
### `server.py`
   <!-- .element: class="fragment" -->
```py
...
from friend import Friend
...
@app.route('/')
def index():
    friends = Friend.get_all()
    print(friends)
    return render_template("index.html", all_friends = friends)
```
   <!-- .element: class="fragment" -->
### `friend.py`
   <!-- .element: class="fragment" -->
```py
class Friend:
...
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM friends;"
        results = connectToMySQL('first_flask').query_db(query)
        friends = []
        for friend in results:
            friends.append( cls(friend) )
        return friends
```
   <!-- .element: class="fragment" -->
---
## queries with variable data
---
## sql injection
--
![](/../../images/sql-inj.png)   <!-- .element: class="r-stretch" width="95%" -->
---
## from form to database
--
## from form to database
```py
from mysqlconnection import connectToMySQL

class Friend:
...
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO friends ( first_name , last_name , occupation , created_at, updated_at ) VALUES ( %(fname)s , %(lname)s , %(occ)s , NOW() , NOW() );"

        return connectToMySQL('first_flask').query_db( query, data )
```
  <!-- .element: data-trim class="r-stretch r-fit-text" -->
---
## MVC
--
![](/../../images/mvc.png)
<!-- .element: data-trim class="r-stretch r-fit-text" -->
<!-- .slide:data-background="#fff" -->
--
![](/../../images/mvc2.png)
<!-- .element: data-trim class="r-stretch r-fit-text" -->
---
## Modularization
--
### We started with three files
1. `server.py`   <!-- .element: class="fragment" -->
2. `mysqlconnection.py`   <!-- .element: class="fragment" -->
3. `model.py`   <!-- .element: class="fragment" -->

--
### Our file structure looked like this:
![](/../../images/pre-mod.png)
<!-- .element:class="r-stretch" -->
<!-- .element:class="fragment" -->
--
![](/../../images/mod1.png)
--
![](/../../images/mod2.png)
--
![](/../../images/mod3.png)
--
![](/../../images/mod4.png)
--
![](/../../images/mod5.png)
--
![](/../../images/mod6.png)
--
![](/../../images/mod7.png)
---
## Controllers
--
## Controllers
- controllers handle routes/requests and <!-- .element: class="fragment" -->
- minimal logic (fat models, skinny controllers) <!-- .element: class="fragment" -->
- access database via models <!-- .element: class="fragment" -->
---
## Models
--
## Models
- models handles logic related to data <!-- .element: class="fragment" -->
- access database via mysqlconnection.py <!-- .element: class="fragment" -->
---
---
## mvc
---
## modularization
---
## controllers
---
## models
---
## users crud modularized (core)
---