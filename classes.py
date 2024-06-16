# Task 1

# The "Human" class.

# Create a class called Person. Make the __init__() method
# took firstname, lastname, and age as parameters and added them as attributes.
# Create another method called talk() that prints a greeting from the person
# which contains, for example, "Hi, my name is Carl Johnson, I'm 26 years old."

class Person:
    def __init__(self,name: str,surname:str,age:int):
        self.name=name
        self.surname=surname
        self.age=age

    def talk(self):
        print(f"Hello, my name is {self.name} {self.surname}, I am {self.age} y.o.")

person_carl=Person("Сarl","Johnson",35)
person_carl.talk()

 

# Task 2

# Dog age

# Create a class Dog with class attribute 'age_factor' equal to 7. Create
# __init__(), which takes the value of the dog's age. Then create a method
# `human_age`, which returns the dog's age in human terms.

class Dog:
    def __init__(self,age:int):
        self.age=age

    def human_age(self,age:int):
        human=age*7
        return human
    
age_factor = Dog(7)
print(age_factor.human_age(7))

# Task 3
# TV controller

# Create a simple prototype TV controller in Python.
# It will use the following commands:

# first_channel() - includes the first channel from the list.
# last_channel() - turns on the last channel from the list.
# turn_channel(N) - turns on the N channel. Please note that channel numbers
# start with 1, not 0.
# next_channel() - turns on the next channel. If the current channel is the last,
# enables the first channel.
# previous_channel() - turns on the previous channel. If the current channel is first,
# enables the last channel.
# current_channel() - returns the name of the current channel.
# exists(N/'name') - takes 1 argument - number N or string 'name' and returns
# "Yes" if channel N or 'name' exists in the list, or "No" otherwise.


# The default channel enabled before all commands is #1.

# Your task is to create the TVController class and the methods described above.

# '''

# CHANNELS = ["BBC", "Discovery", "TV1000"]

# class TVController:

# skip

# controller = TVController(CHANNELS)

# controller.first_channel() == "BBC"

# controller.last_channel() == "TV1000"

# controller.turn_channel(1) == "BBC"

# controller.next_channel() == "Discovery"

# controller.previous_channel() == "BBC"

# controller.current_channel() == "BBC"

# controller.exists(4) == "No"

# controller.exists("BBC") == "Yes"
# '''

class TVController:
    def __init__(self,name:str):
        self.name=name
        

    def first_channel(self):
        
        return channels[0]

    def last_channel(self):
        
        return channels[-1]

    def turn_channel(self):
        N=int(input("Choose your channel (1 or 2 or 3): "))
        return channels [N-1]

    def next_channel(self):
        TV=controller.turn_channel()
        if TV==channels[0]:
            return channels [1]
        elif TV==channels[-1]:
            return channels [0]
        else:
            return channels [-1]

    def previous_channel(self):
        TV=controller.turn_channel()
        if TV==channels[0]:
            return channels [-1]
        elif TV==channels[-1]:
            return channels [-2]
        else:
            return channels [0]

    def current_channel():
        return channels [0]

    def exists(self, name_):
        if name_ in channels:
            return f"YES"
        else:
            return f"NO"


channels = ["BBC", "Discovery", "TV1000"]
controller = TVController(channels) 
bbc=TVController("BBC")
discovery=TVController("Discovery")
tv1000=TVController("TV1000")

# print(f"1-st channel: {controller.first_channel()}")
# print(f"Last channel: {controller.last_channel()}")
# print(f"Your channel: {controller.turn_channel()}")
# print(f"The next channel is: {controller.next_channel()}")
# print(f"The previous channel is: {controller.previous_channel()}")
# print(f"The current channel is:{controller.current_channel()}")"

name_=input("Input channel: ")
print(controller.exists(name_))
