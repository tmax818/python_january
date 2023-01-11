
# # ! Object Oriented Programming - OOP

# # TODO: Class Structure
# ###### constructor method -- `__init__()` ######

# # ? create a `Cat` class with no instance attributes:

# class Cat:
    
#     def __init__(self, color, name):
#         self.name = name
#         self.color = color
#         self.toys = []
#         self.friend = None

        
#     def get_new_toy(self, toy):
#         self.toys.append(toy)
        
#     def make_friends(self, cat):
#         self.friend = cat
    
#     def show_everything(self):
#         print(self.name, self.toys, self.friend)

# luna = Cat("blue", "Luna")
# ralph = Cat("orange", "Ralph")
# # luna.get_new_toy("ball")
# # ralph.get_new_toy("mouse")
# ralph.make_friends(luna)
# # print(luna.toys)
# print(ralph.friend)
# print(luna)



# print(luna)
# print(ralph)


###### instance attributes ######

# ? create a `Dog` class with `name` and `breed` instance attributes:

###### instance methods ######

# ? modify you `Dog` class so your dog instances can bark:

###### Defining a class ######

# ? what is a class???

# TODO: Instances vs Classes

###### creating an instance of the class ######

# ? create an instance of your Dog class

###### self as a reference to the instance ######

# ? add a method to your Dog class that prints `self` to the console.

# TODO: Chaining Methods

###### returning self ######

# ? modify the `bark` method of your Dog class so you can chain
# ? the bark methods like this: fido.bark().bark().bark() will print
# ? "woof woof woof" to the console.  

# TODO: cls with Class Methods
###### Class methods vs Instance Methods ######

# ? create a `Tesla` class:

class Tesla:
    
    LOCATION = "Freemont"
    num_employees = 0
    CEO = "Elon Musk"
    cars = []
    
    def __init__(self, color, model, year):
        self.color = color
        self.model = model
        self.year = year
        self.mileage = 0
        Tesla.cars.append(self)
        
    def drive(self, miles):
        self.mileage += miles
        
    @classmethod
    def display_all_cars(cls):
        for car in cls.cars:
            print(f"color: {car.color}, model: {car.model}, year: {car.year}")
            
    @staticmethod
    def change_tire():
        print("The tire is fixed")
        
    @staticmethod
    def validate_cars_from_list(cars_list):
        valid_car = True
        for car in cars_list:
            if car.feature == 'free-food':
                valid_car = False
        return valid_car
            
cars = [
    {'color': 'black', 'model': 'ModelS', 'feature': 'self-driving'},
    {'color': 'red', 'model': 'ModelY', 'feature': 'free-food'},
]
ahmons_tesla = Tesla("black", "ModelS", 2018)
ahmons_tesla.mileage = 50000
# print(ahmons_tesla)
# ahmons_tesla.drive(100)
# print(ahmons_tesla.mileage)

vera_tesla = Tesla("gold", "3X", 2023)
vera_tesla.change_tire()
# print(vera_tesla)
# vera_tesla.drive(10)
# print(vera_tesla.mileage)
Tesla.display_all_cars()
        
    

# ? give the Tesla an instance method that makes sense(i.e you own a Tesla car, what should the car be able to do?).

###### Passing cls instead of self ######
###### cls is a reference to the class ######

# ? give the Tesla class a class method that it would make sense for Tesla the company to have(i.e Tesla the company doesn't need to brake or accelerate, but it may want to keep track of all the Tesla cars it makes!!)

###### class attributes ######

# ? give the Tesla class a class attribute. What is a noun that applies to Tesla the company, but not necessarily an individual Tesla car?

# TODO: Static Methods
###### Static methods in organizing the code ######
###### Purpose of static methods ######

# TODO: D.R.Y.
###### DON'T REPEAT YOURSELF ######




class Employee:
    
    def __init__(self, name, id) -> None:
        self.name = name
        self.id = id
        
class Doctor(Employee):

    def do_surgery(self):
        print("I am a surgeon")

class Custodian(Employee):
    
    def mop_the_floor(self):
        print("I am cleaning up blood")
        
class Manager(Doctor):
    pass
    