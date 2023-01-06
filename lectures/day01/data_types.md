<section>
<h2>Data Types</h2>
<p class="fragment">primitive</p>
<p class="fragment">composite</p>
</section>

<section>
<h2>Data Types</h2>
<p class="fragment">Why worry about the type of our data?</p>
<img class="fragment" src="./../../images/lockers.jpg" height="400px">
</section>



<section>
<h2>Primitive</h2>
<p class="fragment">Numbers</p>
<p class="fragment">Booleans</p>
<p class="fragment">None</p>
<p class="fragment">Strings</p>
</section>

<section data-auto-animate>
<h2 data-id="code-title">integers</h2>
<pre data-id="code-animation"><code class="hljs" data-trim>
int_number = 42
</code></pre>
</section>

<section data-auto-animate>
<h2 data-id="code-title">floats</h2>
<pre data-id="code-animation"><code class="hljs" data-trim>
int_number = 42
float_number = 3.14
</code></pre>
</section>

<section data-auto-animate>
<h2 data-id="code-title">booleans</h2>
<pre data-id="code-animation"><code class="hljs" data-trim>
is_logged_in = True
</code></pre>
</section>

<section data-auto-animate>
<h2 data-id="code-title">booleans</h2>
<pre data-id="code-animation"><code class="hljs" data-trim>
is_logged_in = False
</code></pre>
</section>

<section data-auto-animate>
<h2 data-id="code-title"><code>None</code></h2>
<pre data-id="code-animation"><code class="hljs" data-trim>
checking_balance = None
</code></pre>
</section>

<section data-auto-animate>
<h2 data-id="code-title"><code>None</code></h2>
<pre data-id="code-animation"><code class="hljs" data-trim>
checking_balance = 0
</code></pre>
</section>

<section data-auto-animate>
<h2 data-id="code-title">strings</h2>
<pre data-id="code-animation"><code class="hljs" data-trim>
name = "Jenny"
</code></pre>
</section>

<section data-auto-animate>
<h2 data-id="code-title">strings</h2>
<pre data-id="code-animation"><code class="hljs" data-trim>
name = "Jenny"
phone = "867-5309"
</code></pre>
</section>

<section data-auto-animate>
<h2 data-id="code-title">strings</h2>
<pre data-id="code-animation"><code class="hljs" data-trim>
name = "Jenny"
phone = "867-5309"
f"{name}, I got your number: {phone}."
</code></pre>
</section>

<section data-auto-animate>
<h2 data-id="code-title">strings</h2>
<pre data-id="code-animation"><code class="hljs" data-trim>
name = "Jenny"
phone = "867-5309"
f"{name}, I got your number: {phone}."
#=> Jenny, I got your number: 867-5309.
</code></pre>
</section>

<section>
<h2>Composite</h2>
<p class="fragment">lists</p>
<p class="fragment">dictionaries</p>
<p class="fragment">tuples</p>
</section>

<section data-auto-animate>
<h2 data-id="code-title">List</h2>
<pre data-id="code-animation"><code class="hljs" data-trim>
fruits = ['apple', 'banana', 'strawberry']
</code></pre>
</section>

<section data-auto-animate>
<h2 data-id="code-title">List</h2>
<pre data-id="code-animation"><code class="hljs" data-trim>
fruits = ['apple', 'banana', 'strawberry']
fruits[2] = 'blueberry'
</code></pre>
</section>

<section data-auto-animate>
<h2 data-id="code-title">List</h2>
<pre data-id="code-animation"><code class="hljs" data-trim>
fruits = ['apple', 'banana', 'strawberry']
fruits[2] = 'blueberry'
print(fruits)
</code></pre>
</section>

<section data-auto-animate>
<h2 data-id="code-title">List</h2>
<pre data-id="code-animation"><code class="hljs" data-trim>
fruits = ['apple', 'banana', 'strawberry']
fruits[2] = 'blueberry'
print(fruits)
#=> ['apple', 'banana', 'blueberry']
</code></pre>
</section>

<section data-auto-animate>
<h2 data-id="code-title">Dictionaries vs Lists</h2>
<pre data-id="code-animation"><code class="hljs" data-trim>
person_list = ['Tyler', 39, True]
</code></pre>
</section>

<section data-auto-animate>
<h2 data-id="code-title">Dictionaries vs Lists</h2>
<pre data-id="code-animation"><code class="hljs" data-trim>
person_list = ['Tyler', 39, True]
person_dict = {'name': 'Tyler', 'age': 39, 'is_admin': True}
</code></pre>
</section>

<section data-auto-animate>
<h2 data-id="code-title">Dictionaries</h2>
<pre data-id="code-animation"><code class="hljs" data-trim>
person_list = ['Tyler', 39, True]
person_list[0]
person_dict = {'name': 'Tyler', 'age': 39, 'is_admin': True}
</code></pre>
</section>

<section data-auto-animate>
<h2 data-id="code-title">Dictionaries</h2>
<pre data-id="code-animation"><code class="hljs" data-trim>
person_list = ['Tyler', 39, True]
person_list[0]
# => 'Tyler'
person_dict = {'name': 'Tyler', 'age': 39, 'is_admin': True}
</code></pre>
</section>

<section data-auto-animate>
<h2 data-id="code-title">Dictionaries</h2>
<pre data-id="code-animation"><code class="hljs" data-trim>
person_list = ['Tyler', 39, True]
person_list[0]
# => 'Tyler'
person_dict = {'name': 'Tyler', 'age': 39, 'is_admin': True}
person_dict['name']
</code></pre>
</section>

<section data-auto-animate>
<h2 data-id="code-title">Dictionaries</h2>
<pre data-id="code-animation"><code class="hljs" data-trim>
person_list = ['Tyler', 39, True]
person_list[0]
# => 'Tyler'
person_dict = {'name': 'Tyler', 'age': 39, 'is_admin': True}
person_dict['name']
# => 'Tyler'
</code></pre>
</section>

<section data-auto-animate>
<h2 data-id="code-title">Dictionaries</h2>
<pre data-id="code-animation"><code class="hljs" data-trim>
person_list = ['Tyler', 39, True]
person_list[0]
# => 'Tyler'
person_dict = {0: 'Tyler', 1: 39, 2: True}
person_dict[0]
# => 'Tyler'
</code></pre>
</section>