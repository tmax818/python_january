![](../../images/coding_dojo_logo_white.png)
<!-- .slide:data-background="#000000" -->
---
# MySQL Queries
---
## SQL
--
### Intro to SQL

--

### Intro to SQL
- Structured Query Language <!-- .element: class="fragment" -->
- SQL statements aka queries can: <!-- .element: class="fragment" -->
  - SELECT <!-- .element: class="fragment" -->
  - INSERT <!-- .element: class="fragment" -->
  - UPDATE <!-- .element: class="fragment" -->
  - DELETE <!-- .element: class="fragment" -->
--
### Database and SQL
![](../../images/sql-icon.png) 


---
## Connecting to MySQL
--
- **MySQL server** is a database server listening on `localhost`
- we also have a web server listening on `localhost`
- They are listening on different ports
--
---
## Import
--
## Import

### two ways<!-- .element: class="fragment" -->

- copy and paste a sql file <!-- .element: class="fragment" -->
- forward engineer an ERD diagram <!-- .element: class="fragment" -->
---
# CRUD
--
# CRUD

- Create <!-- .element: class="fragment" -->
- Read <!-- .element: class="fragment" -->
- Update <!-- .element: class="fragment" -->
- Delete <!-- .element: class="fragment" -->
--
- Create = `INSERT` <!-- .element: class="fragment" -->
- Read = `SELECT`<!-- .element: class="fragment" -->
- Update = `UPDATE`<!-- .element: class="fragment" -->
- Delete = `DELETE`<!-- .element: class="fragment" -->
---
## `SELECT`
--
```sql
SELECT * FROM table_names; 
```
- select everything from table_names <!-- .element: class="fragment" -->
--

```sql
SELECT column_name FROM table_names; 
```
- select column_name from table_names <!-- .element: class="fragment" -->
--
```sql
SELECT column_name1, column_name2 FROM table_names; 
```
- select column_name1 and column_name2 from table_names <!-- .element: class="fragment" -->
--
### `SELECT` with Conditionals
--
```sql
SELECT column_name1 
FROM table_names 
WHERE id = 2;
```

- select the record in column_name1 from table_names with an id of 2. <!-- .element: class="fragment" -->
--

```sql
SELECT column_name1 
FROM table_names 
WHERE id = 2 OR id = 3;
```

- select the record in column_name1 from table_names with an id of 2 or 3. <!-- .element: class="fragment" -->
--

```sql
SELECT *
FROM table_names 
WHERE column_name LIKE "%e";
```

- select everything from table_names in column name that ends with e. <!-- .element: class="fragment" -->
--

```sql
SELECT *
FROM table_names 
WHERE column_name LIKE "M%";
```

- select everything from table_names in column name that starts with M. <!-- .element: class="fragment" -->
--

```sql
SELECT *
FROM table_names 
WHERE column_name <> "M%";
```

- select everything from table_names in column name that does not start with M. <!-- .element: class="fragment" -->
--
### `SELECT` with Sorting
--
```sql
SELECT *
FROM table_names 
ORDER BY column_name DESC;
```
- select everything from table_names order by column name in descending order. <!-- .element: class="fragment" -->
--
```sql
SELECT *
FROM table_names 
ORDER BY column_name ASC;
```
- select everything from table_names order by column name in ascending order. <!-- .element: class="fragment" -->

### `SELECT` with limit and offset
--
```sql
SELECT *
FROM table_names 
LIMIT 3;
```
- select the first three table_names <!-- .element: class="fragment" -->

---
## `INSERT`
--

```sql
INSERT INTO table_name (column_name1, column_name2) 
VALUES('column1_value', 'column2_value');
```

---
## `UPDATE`
--

```sql
UPDATE table_name 
SET column_name1 = 'some_value', column_name2='another_value' 
WHERE condition(s)
```
--
>IMPORTANT: if WHERE condition is not added to the UPDATE statement, the changes will be applied to every record in the table.
---
## `DELETE`
--

```sql
DELETE FROM table_name (column_name1, column_name2) 
VALUES('column1_value', 'column2_value') WHERE id = id;
```
---
## Functions
---
## Joins
--

![](../../images/types_joins.webp)

--
>We JOIN two tables on the ids (i.e. the primary key and the foreign key) that match each other. This means that we can't JOIN tables together that don't have a relationship with each other (e.g. One to One, One to Many, Many to Many).
--
### one to one

```sql
SELECT * FROM customers 
JOIN addresses ON addresses.id = customers.address_id;
```  
<!-- .element: class="fragment" -->
![](../../images/one-to-one4.png)  <!-- .element: class="fragment" -->
![](../../images/one-to-one.gif)  <!-- .element: class="fragment" -->

--
### one to many
```sql
SELECT * FROM orders 
JOIN customers ON customers.id = orders.customer_id;
```  
<!-- .element: class="fragment" -->
![](../../images/one-many4.png)  <!-- .element: class="fragment" -->
--
![](../../images/one-many.gif)  <!-- .element: class="r-fit" -->
--

### many to many
```sql
SELECT * FROM orders 
JOIN items_orders ON orders.id = items_orders.order_id 
JOIN items ON items.id = items_orders.item_id;
```  
<!-- .element: class="fragment" -->
![](../../images/m-m4.png)  <!-- .element: class="fragment" -->
--
![](../../images/m-m.gif)  <!-- .element: class="r-fit" -->
--

---
## Left Joins
DEMO
---
## Export
---
## Forward Engineer
---
## MySQL Workbench Setup (Practice)
---
## Users (Practice)
---
## Dojo and Ninjas (Core)
---
## Friendships (Practice)
---
## MySQL Countries (Core)

