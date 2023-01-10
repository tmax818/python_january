
# # ! Python Fundamentals

# ##### Python Syntax ########

# # TODO: Indentation, code blocks, pass

# # ? add a code block to the function below
# def my_func():
#     print("hello")
#     print('goodbye')

# # ? add a code block to the for loop below
# # ? so that 'hello' and 'world' print to the console
# # ? 100 times on separate lines:
# # ? hello
# # ? world
# # ? hello
# # ? world
# # ? ...

# for i in range(100):
#     pass

# if True:
#     pass

# #### Data Types #######

# # TODO: Primitive
# ##### Integers #####

# # ? define a variable `my_int` and assign your favorite number to it

# my_int = 42

# # ? define a variable `my_float` and assign the value of pi to it



# ##### Booleans #####
# ##### None ##### 
# ##### Strings #####

# # ? write the three ways to create the string "The knights who say, 'Ni!'" in Python:

# str1 = "The knights who say, 'Ni!'"
# print(str1)
# str2 = 'The kningts who say, "Ni"'
# str3 = """The knights 
# who say, 'Ni'"""
# print(str3)



# # TODO: Composite

# ##### Lists #######
# num_list = [0,1,2,3,4,5]

# # ? add the number 6 to the `num_list` using a builtin list method
# # ? add a test to make sure it worked!!!

# color_list = ['red', 'orange', 'yellow']

# # ? add 'green' to color_list.
# color_list.append('green')
# # print(color_list)
# # ? add a test to make sure it worked!!!
# weird_list = ['Tyler', True, [42, 35, 7, 13, 6], 0, None, {'password': 'catcrazy76' }]

# # print(weird_list[2][2])
# ###### Dictionaries ########

# person_list = ['Tyler', 39, True]
# # print(person_list[1])

# person_dict = {'name': 'Tyler', 'age': 39, 'is_cool': True}
# # print(person_dict['age'])
# person_dict['hobbies'] = ['coding', 'sleeping']
# print(person_dict)
# person_dict['hobbies'].append('reading')
# print(person_dict['hobbies'])
# ###### Lists of Dictionaries ###########





# ###### Tuples #######
# person_tup = 'Tyler', 39, True

# # ? How many methods are available for `person_tup` in Python?



# # TODO: Conditionals
# ###### if, elif, else
# ###### chaining conditional statements

# condition1 = True
# condition2 = True

# if condition1:
#     print("eggs and spam")
# elif condition2:
#     print("Tyler is cool!")
# else:
#     print("Lucky is cooler than Tyler!")

# # TODO: Loops
# ###### for loops

# # ? write a while loop that will print "I love Python" 100 times
# i = 0
# while i < 11:
#     print('I love Python')
#     i += 1
    

# # ? write a for loop that will print "I really love Python" 100 times
# for i in range(1, 11, 2):
#     print(i)

# ###### using with range

# # ? write a for loop using the builtin range() function

# my_range = range(10)
# print(my_range)

# ###### using with composite types

# # ? write three for loops to loop through `person_list`, `person_dict` and `person_tup`:

# # person_list = ['Tyler', 39, True]
# # person_dict = {'name': 'Tyler', 'age': 39, 'is_cool': True}
# # person_tup = 'Tyler', 39, True


# #TODO: Built In Methods
# ###### print()

# # ? create a variable called `message` and use the `print()` method to print the message
# # ? to the console.
# message = "spam and eggs"
# ###### len()
# print(len(message))
# # ? use the `len()` method to print the length of the `message` variable defined above.

# ###### conversions: str(), int()

# # ? create a variable `age` as an int. Use one of the conversion 
# # ? methods above to change it to a string. 

# ###### range()

# # ? create a variable `my_range` and set it equal to the invocation of the builtin range function that will iterate 10 times.

# def my_func():
#     print("testing")
    
# my_func()

# # TODO: Functions
# ###### parameters vs. arguments

# def param_arg_func(parameter):
#     the_parameter = parameter
#     print(the_parameter)
    
# param_arg_func("argument")


# ###### return vs. print

def return_func(params):
    return params
    print(params)

def print_func(params):
    print(params)
    return(params)
    
ret = return_func("Lucky is cool")
pri = print_func("Tyler is cool")

print("ret = ",ret)
print("pri = ", pri)


def say_hello(name="Python Programmer"):
    print(f"hello {name}")
    print("hello {}".format(name))
    print("hello %s" % (name))
    
say_hello("Nima")
say_hello("Lucky")
say_hello()