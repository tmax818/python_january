![](../../images/coding_dojo_logo_white.png)
<!-- .slide:data-background="#000000" -->
---
# ERD Lesson

Note:

- ERD = entity relation diagram 
---
## overview
Note:
10,000 foot view
--
![](../../images/full_stack.png)

Note:

- started with the front end
- left off on Friday with backend
- today we are adding the final piece
--

## What is a database?
<!-- .slide:data-background="#000000" -->
Note:
- what's a database
- most common analogy is the spreadsheet
- databases are made of as many tables as we need
--
<!-- .slide:data-background="#000000" -->
![](../../images/spreadsheet.png)

Note:
- we use spreadsheets to store data
- a spreadsheet is like a table in a database
--
## Why not just use a spreadsheet?
Note:
- what if we had a million students
- 1 million seconds in 12 days!!
--
## Why MySQL and database design?
<!-- .slide:data-background="#000000" -->
![](../../images/mysql.png)

Note:
- we start with sql databases
- in MERN we learn no-sql databases
- a db is the backbone of your web app
--
![](../../images/mysql-pop.png)

Note:
- dbs allow us to move beyond sessions/cookies
--
Databases allow us to persist our data.
--
### databases also allow us to:
- create, save and manipulate data:
  - access, manage and update
--

### Goals
- minimize repetition
- minimize data queries

--

## Why ERD first?
- 'Entity Relationship Diagram' <!-- .element: class="fragment" -->
- visual plans  <!-- .element: class="fragment" -->
- map of the structure of data storage  <!-- .element: class="fragment" -->
- define relationships  <!-- .element: class="fragment" -->

![](../../images/books.png) <!-- .element: class="fragment" -->

Note:
- a graphical tool that generates SQL from our diagrams/ERDs
--

>Learning the design of the database first will help us visualize what our relational databases look like, which makes it much easier to choose the actual SQL syntax.


---
## database design
--

### principles of database design:

- reduce data repetition <!-- .element: class="fragment" -->  
- one table for each real world object*  <!-- .element: class="fragment" -->
- one column for each of the object's attributes  <!-- .element: class="fragment" -->
- decide the relationships between the objects/tables  <!-- .element: class="fragment" -->
Note:
- normalization make extra tables
--
![](../../images/db-sample.png)

Note:
- first column is the id = primary key
- the pk is how we organize/differentiate and access rows

---
<!-- .slide:data-background="#000000" -->
# Database Relations

---
## one to one
--
## one to one
![](../../images/one-to-one.png) <!-- .element: class="fragment" -->
![](../../images/one-to-one2.png) <!-- .element: class="fragment" -->
![](../../images/one-to-one3.png) <!-- .element: class="fragment" -->
Note:
- one or two true one-to-one
- data privacy/security
- foreign key = shows ownership
- fk allows us to join tables in db
--
YAGNI

---
## one to many
--
## one to many
- most common <!-- .element: class="fragment" -->
![](../../images/one-many1.png) <!-- .element: class="fragment" -->
![](../../images/one-many2.png) <!-- .element: class="fragment" -->
Note:
- a customer has many orders
- order in a restaurant or amazon
- who has the most orders of the three customers?
---
## many to many
--
## many to many
![](../../images/m-m1.png) <!-- .element: class="fragment" -->
![](../../images/m-m2.png) <!-- .element: class="fragment" -->
![](../../images/m-m3.png) <!-- .element: class="fragment" -->
Note:
- many-to-many === join table
--
- create a connector table(aka join table)  <!-- .element: class="fragment" -->
- can be confusing, talk out the relationship out loud
---
## normalization
-- 
### What is normalization?
-- 
>Database normalization is simply a convention for splitting large tables of data into smaller separate tables with the primary goal being to not repeat data.
--
<!-- .slide:data-transition="convex-in concave out" -->
# **It is possible to take normalization to an extreme.**
--
## The three forms:
Note:
- cumulative
- they build on each other
--
### First Form
- one column, one value  <!-- .element: class="fragment" -->

![](../../../../../../images/one-to-one.png)  <!-- .element: class="fragment" -->
![](../../../../../../images/one-to-one4.png)  <!-- .element: class="fragment" -->
--
### Second Form

- each column should have a unique value  <!-- .element: class="fragment" -->
  - except for keys  <!-- .element: class="fragment" -->
  - This form can be taken too far!!!!  <!-- .element: class="fragment" -->
![](../../images/one-many4.png)
--

### Third Form
- no column should depend on another  <!-- .element: class="fragment" -->
  - except for keys  <!-- .element: class="fragment" -->
  - This form can be taken too far!!!!  <!-- .element: class="fragment" -->
![](../../../../../../images/one-to-one4.png)  <!-- .element: class="fragment" -->
---
## conventions
--
## conventions
1. table names are plural and lower case (i.e. users, sites, clients)
2. use `id` as the primary key
3. name foreign keys with singular table name(i.e. user_id, site_id, client_id)
4. use `created_at` and `updated_at` on EVERY table you create.

---
## data types
--
# `VARCHAR`
- up to 255 characters.
- will store variable number of characters
--
# `CHAR`
- up to 255 characters.
- will store all space reserved
--
# `INT`
- up to 4,294,967,295
- signed or unsigned
--
# `BIGINT`
- up to 18,446,744,073,709,551,615
- signed or unsigned
--
# `TINYINT`
- up to 255
- signed or unsigned
--
# `FLOAT` 
- used for decimal numbers
- signed or unsigned
--
# `TEXT`
- stores text
- stores text that `VARCHAR()` is too small to handle
--
# `DATETIME`
- stores dates
- format `YYYY-MM-DD hh:mm:ss`
---
## simple blog
--
![](./files/simple_blog/blog.svg)
  <!-- .element: class="r-stretch" " -->
---
## likes
---
## yelp
---
## amazon
---
## belts
---
## [users practice](https://login.codingdojo.com/m/172/7217/54135)
--
# [DEMO](./files/users_practice/README.md)
---
## dojos and ninjas cores core
---
## books core
---
## friendships practice
---