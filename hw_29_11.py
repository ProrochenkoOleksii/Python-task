# Завдання 1

# Клас «Людина».

# Створіть клас під назвою Person. Зробіть так, щоб метод __init__() 
# приймав ім’я, прізвище та вік як параметри та додавав їх як атрибути.
# Створіть інший метод під назвою talk(), який друкує привітання від особи, 
# яке містить, наприклад, таке: «Привіт, мене звати Карл Джонсон, мені 26 років».

# class Person:
#     def __init__(self,name: str,surname:str,age:int):
#         self.name=name
#         self.surname=surname
#         self.age=age

#     def talk(self):
#         print(f"Hello, my name is {self.name} {self.surname}, I am {self.age} y.o.")

# person_carl=Person("Сarl","Johnson",35)
# person_carl.talk()

 

# Завдання 2

# Собачий вік

# Створіть клас Dog з атрибутом класу 'age_factor', рівним 7. Створіть 
# __init__(), який приймає значення віку собаки. Потім створіть метод
# `human_age`, який повертає вік собаки в людському еквіваленті.

# class Dog:
#     def __init__(self,age:int):
#         self.age=age

#     def human_age(self,age:int):
#         human=age*7
#         return human
    
# age_factor = Dog(7)
# print(age_factor.human_age(7))

# Завдання 3
# ТВ контролер

# Створіть простий прототип телевізійного контролера на Python. 
# Він використовуватиме такі команди:

# first_channel() - включає перший канал зі списку.
# last_channel() - вмикає останній канал зі списку.
# turn_channel(N) - вмикає N канал. Зверніть увагу, що номери каналів 
# починаються з 1, а не з 0.
# next_channel() - вмикає наступний канал. Якщо поточний канал є останнім,
# вмикає перший канал.
# previous_channel() - вмикає попередній канал. Якщо поточний канал є першим, 
# вмикає останній канал.
# current_channel() - повертає назву поточного каналу.
# exists(N/'name') - отримує 1 аргумент - число N або рядок 'name' і повертає
# "Так", якщо канал N або 'name' існує в списку, або "Ні" - в іншому випадку.
 

# Канал за замовчуванням, увімкнений перед усіма командами, — №1.

# Ваше завдання — створити клас TVController і методи, описані вище.

# '''

# КАНАЛИ = ["BBC", "Discovery", "TV1000"]

#  клас TVController:

# пропуск

#  контролер = TVController(КАНАЛИ)

# controller.first_channel() == "BBC"

# controller.last_channel() == "TV1000"

# controller.turn_channel(1) == "BBC"

# controller.next_channel() == "Discovery"

# controller.previous_channel() == "BBC"

# controller.current_channel() == "BBC"

# controller.exists(4) == "Ні"

# controller.exists("BBC") == "Так"

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