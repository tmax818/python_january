# Python Syntax

- [REPL demo](http://localhost:8888/notebooks/demo.ipynb)
--
## Indentation and Blocks of Code

- Python uses indentation and the colon(:) to indicate blocks of code.  <!-- .element: class="fragment" -->
--
## What is a code block?
--
# Indentation
```py
for i in range(100):
print("hello")
```
 <!-- .element: class="fragment fade-in" -->

```bash
File "fundamentals.py", line 2
    print("say hello")
    ^
IndentationError: expected an indented 
block after 'for' statement on line 1
```
 <!-- .element: class="fragment fade-in" -->


```py
for i in range(100):
    print("hello")
```
 <!-- .element: class="fragment fade-in" -->

--
## `pass` keyword

```py
for i in range(100):
    pass
```
 <!-- .element: class="fragment fade-in" -->