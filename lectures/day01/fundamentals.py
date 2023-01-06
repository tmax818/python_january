
# ! Python Fundamentals

##### Python Syntax ########

# TODO: Indentation, code blocks, pass

# ? add a code block to the function below
def my_func():
    pass

# ? add a code block to the for loop below
# ? so that 'hello' and 'world' print to the console
# ? 100 times on separate lines:
# ? hello
# ? world
# ? hello
# ? world
# ? ...

for i in range(100):
    pass

if True:
    pass

#### Data Types #######

# TODO: Primitive
##### Integers #####

# ? define a variable `my_int` and assign your favorite number to it

# ? define a variable `my_float` and assign the value of pi to it

##### Booleans ##### 
##### None ##### 
##### Strings #####

# ? write the three ways to create the string `eggs and spam` in Python:



# TODO: Composite

##### Lists #######
num_list = [0,1,2,3,4,5]

# ? add the number 6 to the `num_list` using a builtin list method
# ? add a test to make sure it worked!!!

color_list = ['red', 'orange', 'yellow']

# ? add 'green' to color_list. 
# ? add a test to make sure it worked!!!
weird_list = ['Tyler', True, [42, 35, 7, 13, 6], 0, None, {'password': 'catcrazy76' }]

###### Dictionaries ########

person_list = ['Tyler', 39, True]
person_dict = {'name': 'Tyler', 'age': 39, 'is_cool': True}

###### Lists of Dictionaries ###########





###### Tuples #######
person_tup = 'Tyler', 39, True

# ? How many methods are available for `person_tup` in Python?



# TODO: Conditionals
###### if, elif, else
###### chaining conditional statements

condition1 = True
condition2 = True

if condition1:
    print("eggs and spam")
elif condition2:
    print("Tyler is cool!")
else:
    print("Lucky is cooler than Tyler!")

# TODO: Loops
###### for loops

# ? write a while loop that will print "I love Python" 100 times
# ? write a for loop that will print "I really love Python" 100 times

###### using with range
###### using with composite types



#TODO: Built In Methods
###### print()

# ? create a variable called `message` and use the `print()` method to print the message
# ? to the console.

###### len()

# ? use the `len()` method to print the length of the `message` variable defined above.

###### conversions: str(), int()

# ? create a variable `age` as an int. Use one of the conversion 
# ? methods above to change it to a string. 

###### range()


# TODO: Functions
###### parameters vs. arguments

def param_arg_func(parameter):
    the_parameter = parameter
    print(the_parameter)
    
param_arg_func("argument")


###### return vs. print

def return_func():
    pass

def print_func():
    pass



