# Conditionals
--
>Conditional statements allow us to run certain lines of code depending on whether certain conditions are met. 
--

--
If we want to execute code if some condition is true:
```py
if (some condition that evaluates to True or False):
    # if it's True, the code in here will run
```
notice the indentation
<!-- .element: class="fragment" -->
--
--
If we want to execute code if some condition is true and do something else if it's false:
```py
if (some condition that evaluates to True or False):
    # if it's True, the code in here will run
else:
    # if it's False, the code in here will run
```
--

--
If we want to check multiple things:
```py
if (some condition that evaluates to True or False):
    # if it's True, the code in here will run
elif (some condition that evaluates to True or False):
    # code in here will run if the conditions above it are False
else:
    # if all the above conditions are False, the code in here will run
```
--
```py
condition = True
if condition:
    print("this is true")
```

```bash
this is true
```
<!-- .element: class="fragment" -->
--
```py
expression = "Something that returns a value."
if expression:
    print("Will this print?")
print("...or will this?")
```

```bash
Will this print?
...or will this?
```
<!-- .element: class="fragment" -->
--
```py
if not True:
    print("this ran...")
print("no this ran!!!")
```

```bash
no this ran!!!
```
<!-- .element: class="fragment" -->
--
```py
if not False:
    print("this ran...")
print("no this ran!!!")
```
```bash
this ran...
no this ran!!!
```
<!-- .element: class="fragment" -->
--
```py
if not True:
    print("this ran...")
else:
    print("no this ran!!!")
print("of course this ran, it's outside the conditional!!!")
```
```bash
this ran!!!
of course this ran, it's outside the conditional!!!
```
<!-- .element: class="fragment" -->
--
```py
if not True:
    print("this ran...")
elif True:
    print("the elif ran...")
else:
    print("no this ran!!!")
print("of course this ran, it's outside the conditional!!!")
```
```bash
the elif ran...
of course this ran, it's outside the conditional!!!
```
<!-- .element: class="fragment" -->
---
# Loops
--
## `for` loops with range
--
compare with JavaScript
```javascript
for(var i = 0; i < 10; i++) {
    console.log(i)
}
```
```bash
0
1
2
3
4
5
6
7
8
9
```
<!-- .element: class="fragment" -->
--
same code in Python:
```py
for i in range(10):
    print(i)
```
```bash
0
1
2
3
4
5
6
7
8
9
```
<!-- .element: class="fragment" -->
--
### range with 2 args:
```py
start = 0 # inclusive
stop = 10 # exclusive
step = 2
for i in range(start, stop, step):
    print(i)
```
```bash
0
2
4
6
8
```
<!-- .element: class="fragment" -->


