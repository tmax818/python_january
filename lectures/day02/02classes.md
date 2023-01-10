# classes
--

>"We need to start thinking about classes as blueprints for our custom objects. They aren't the actual objects, but a plan for what properties and functionalities they may have.  We can now create custom objects to suit the need of our web applications!"
--


# class definition
--

```py
class User:
    pass

```
  <!-- .element: class="fragment fade-in" -->
--
# class instantiation
--
```py
user1 = User()
```
---
# Attributes
--
attribute = characteristic
--

```py
class Dojo:
  def __init__(self, location):
    self.location = location
    self.ninjas = []
```
<!-- .element: class="fragment fade-in" -->
--

```py
class Ninja:
  def __init__(self, name, age):
    self.name = name
    self.age = age
```
<!-- .element: class="fragment fade-in" -->
--
```py
dojo1 = Dojo('Burbank')
dojo2 = Dojo('San Jose')
```
<!-- .element: class="fragment fade-in" -->

```py
print(dojo1.location)
```
<!-- .element: class="fragment fade-in" -->

```
Burbank
```
  <!-- .element: class="fragment fade-in" -->
--

```py
ninja1 = Ninja('Nima', 24)
ninja2 = Ninja('Ruwaida', 26)
ninja3 = Ninja('Ahmon', 23)
```
<!-- .element: class="fragment fade-in" -->

```py
print(ninja1.name)
```
<!-- .element: class="fragment fade-in" -->

```
Eric
```
  <!-- .element: class="fragment fade-in" -->
---

# Methods
--
method = action
--

```py
class Dojo:
  def __init__(self, location):
    self.location = location
    self.ninjas = []
```
```py
  def register_ninja(self, ninja):
    self.ninjas.append(ninja)
```
<!-- .element: class="fragment fade-in" -->

--

The `register_ninja` method performs an action. It adds a ninja to that dojo's roster

```py
dojo1.register_ninja(ninja1)
```
<!-- .element: class="fragment fade-in" -->

```py
print(dojo1.ninjas)
```
<!-- .element: class="fragment fade-in" -->

```
[<__main__.Ninja object at 0x0000019E2833BE50>]
```
<!-- .element: class="fragment fade-in" -->

