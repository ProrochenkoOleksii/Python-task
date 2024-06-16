# Task 1

# School

# Create a class structure in Python to represent the people in the school.
# Create a base class called Person, a class called Student, and another class
# named Teacher. Try to find as many methods and attributes as possible,
# that belong to different classes, and keep in mind which ones are common,
# and which ones are not. For example, name should be a Person attribute, while salary should be
# be available only to the teacher.

class Person:
    def __init__(self, name, science):
        self.name = name
        self.science = science


class Student(Person):
    def __init__ (self, name, science, groupe, age):
        super().__init__(name, science)
        self.science = science
        self.groupe = groupe
        self.age = age

    def print_info(self):
        attributes = vars(self)
        print("This is student's info: ")
        for attribute, value in attributes.items():
            print (f'{attribute}: {value}')


class Teacher(Person):
    def __init__(self, name, science, experience, salary_year):
        super().__init__(name, science)
        self.science = science
        self.experience = experience
        self.salary_year = salary_year

    def print_info(self):
        attributes = vars(self)
        print("This is teacher's info: ")
        for attribute, value in attributes.items():
            print (f'{attribute}: {value}')

student1=Student("john", "math", 3456, 18)
student2=Student("peter", "biology", 2059, 19)

teacher1=Teacher("kris", "math", 12, 11000)
teacher2=Teacher("james", "filology", 20, 23000)

student1.print_info()
teacher2.print_info()


# Task 2

# Mathematician

# Implement the Mathematician class, which is a helper class for execution
# mathematical operations with lists
# The class does not accept any attributes and only has methods:

# square_nums (takes a list of integers and returns a list of squares)
# remove_positives (takes a list of integers and returns it without positives
# filter_leaps (takes a list of dates (integers) and removes those that are not
# are "leap years"


class Mathematician ():

    def square_nums(self, my_list1):
        new_list=list()
        for elements in my_list1:
            elements_new=elements**2
            new_list.append(elements_new)
        return new_list
    
    def remove_positives(self, my_list2):
        new_list=list()
        for elements in my_list2:
            if elements<0:
                new_list.append(elements)
            else:
                pass
        return new_list
    
    def filter_leaps(self, my_list3):
        new_list=list()
        for elements in my_list3:
            if (elements % 4 == 0 and elements % 100 != 0) or elements % 400 == 0:
                new_list.append(elements)
            else:
                pass
        return new_list

m = Mathematician()
my_list1=[7, 11, 5, 4]
print(m.square_nums(my_list1))

my_list2=[26, -11, -8, 13, -90]
print(m.remove_positives(my_list2))

my_list3=[2001, 1884, 1995, 2003, 2020]
print(m.filter_leaps(my_list3))


# Task 3
# Shop goods
# Write a Product class that has three attributes:

# type
# name
# price
# Then create a ProductStore class that will have multiple products and
# will work with all products in the store. All methods if they can't
# perform their action, must raise ValueError with the appropriate information
# about an error.

# Hints. Use aggregation/composition concepts during implementation
# of the ProductStore class. You can also implement additional classes to work with
# with a certain type of product, etc.

# In addition, the ProductStore class must have the following methods:

# add(product, quantity) - adds the specified quantity of one product from previously
# a certain price premium for your store (30 percent)
# set_discount(identifier, percent, identifier_type='name') - adds a discount
# for all goods indicated by the entered identifiers (type or name).
# The discount must be specified as a percentage
# sell_product(product_name, amount) - removes a certain number of products from
# of the store, if any, otherwise throws an error. He too
# increases revenue if the sell_product method completes successfully.
# get_income() - returns the amount of many earned by the ProductStore instance.
# get_all_products() - returns information about all available products in the store.
# get_product_info(product_name) - returns a tuple with the name of the product and
# by the number of products in the store.

# assert s.get_product_info('Ramen') == ('Ramen', 290)

class Product():
    def __init__(self,type,name,price):
        self.type = type
        self.name = name
        self.price = price

    def __str__(self):
        return f"Product: {self.name}\n Price: {self.price}\n"

class ProductStore():
    def __init__(self,store_name):
        self.store_name = store_name
        self.product = {} # dict для продуктів і кількості з ціною
        

    def add(self,product,amount):
        self.product[product]=amount,product.price*1.3
        return (f"{amount} {product.name} added to {self.store_name}\n")

    def __str__(self):
        return f"{self.product} in {self.store_name}\n"
    
    # def set_discount(identifier, percent, identifier_type='name'):

    # def sell_product(product_name, amount):

    def get_income(self):
        list_amount=list()
        for key in self.product:
            list_amount.append(self.product[key])
        # print (list_amount)
        list_for_res=list()
        for tuples in list_amount:
            list_for_res.append(tuples[0]*tuples[-1])
            # print(round(tuples[-1],2))
        our_income=0
        for el in list_for_res:
            our_income+=el
        print(f"Income $: {our_income}\n")
        
    def get_all_products(self):
        for elem in self.product:
            for key, value in self.product.items():
                # print(elem.name)

                print(f"{elem.name} - Amount: {value[0]}. Price: {round(value[-1],2)}")
                

    def get_product_info(self,product_name):
        new_tuple=tuple()
        for key, value in self.product.items():
            if product_name==key:
                new_tuple=product_name
                new_tuple=value[0]
                print (new_tuple)
            



p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Ramen', 1.5)
p3 = Product("Fruits", "Bananas", 3)
s = ProductStore("MyStore")
s.add(p,10)
s.add(p2,30)
s.add(p3,100)
# # print(s.__str__())
# s.get_all_products()

# s.get_income()
info_=s.get_product_info("Football T-Shirt")
print(info_)


# Task 4

# Special exception

# Create a custom exception called "CustomException" that can
# inherit from the Exception base class, but extend it
# functionality to log each error message
# in a file called "logs.txt". Tips: Use the __init__ method,
# to extend functionality for saving messages to a file

class Exception():
    def __init__(self,msg):
        self.message = msg

class CustomException(Exception):
    
    def __init__(self,msg):
        super().__init__(msg)
        self.msg = msg

    def my_log(self):
        with open ("file_practice/logs.txt", "w") as myfile:
            myfile.write(f"{self.msg}")    

msg = "message about exception"

try:
    raise CustomException()

except Exception:  
    print("my exception")

# Task 5

# Method overloading.

# Create a base class called Animal with a method called talk,
# and then create two subclasses: Dog and Cat and make their own implementation
# of the talk method by another. For example, a dog can type "woof woof",
# and the cat's "meow".

# Also, create a simple generic function that takes as input
# instance of the Cat or Dog classes and executes the talk method on the input parameter.

class Animal():
    def __init__(self,animal):
        self.animal = animal
    
    def talk(self):
        if animal=="Dog":
            return f"{self.animal} say: 'gav-gav'"
        elif animal=="Cat":
            return f"{self.animal} say: 'myau-myau'"
        else:
            return f"{self.animal} can not speak :-)"



class Dog(Animal):
    def __init__(self,type):
        self.type = type

    def talk(self):
        return f"{self.type} say: 'gav-gav'"


class Cat(Animal):
    def __init__(self,type):
        self.type = type

    def talk(self):
        return f"{self.type} say: 'myau-myau'"

animal=Animal("Bird")
dog1=Dog("My dog")
cat1=Cat("My cat")
print(cat1.talk())
print(dog1.talk())
print(animal.talk())


# Task 6

# Library
# Write a class structure that implements the library. Classes:
# 1) Library - name, books = [], authors = []
# 2) Book – title, year, author (the author must be an instance of the Author class)
# 3) Author - name, country, birthday, books = []

# Library class
# Methods:
# - new_book(name: str, year: int, author: Author) - returns an instance
# of the Book class and adds the book to the list of books for the current library.
# - group_by_author(author: Author) - returns a list of all grouped books
# by the specified author
# - group_by_year(year: int) - returns a list of all books grouped by
# in the specified year

# All 3 classes must have readable __repr__ and __str__ methods.
# Also, the book class must have a class variable that contains the count
# of all existing books

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def new_book(self, title, year, authors):
        book = Book(title=title, year=year, authors=authors)
        self.books.append(book)
        return book

    def __str__(self):
        book_info = "\n".join(str(book) for book in self.books)
        return f"This is the library with the following books:\n{book_info}"


    def group_by_author(self, author):
        return [book for book in self.books if author == book.authors]

    def group_by_year(self, year):
        return [book for book in self.books if book.year == year]


class Book:
    def __init__(self, title, year, authors):
        self.title = title
        self.year = year
        self.authors = authors

    def __repr__(self):
        return f"Book(title='{self.title}', year={self.year}, authors={self.authors})"

    def __str__(self):
        return f"{self.title} ({self.year}), Authors: {self.authors}"

class Author:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}"


author1=Author("Franko")
author2=Author("Eco")
author3=Author("Chase")
book1=Book("Zahar Berkut",1885,author1)
book2=Book("Rose's name",1980,author2)
book3=Book("Baudolino",2000,author2)
book4=Book("Only cash",1939,author3)

library=Library(name="My Library")

library.new_book("Zahar Berkut",1885,author1)
library.new_book("Rose's name",1980,author2)
library.new_book("Baudolino",2000,author2)

print(library)

var_author=library.group_by_author(author1)
var_year=library.group_by_year(2000)
print(var_year)
print(var_author)

# Task 7
# fraction
# Create a Fraction class that will represent all basic arithmetic
# logic for fractions (+, -, /, *) with proper error checking and handling.
# Need to add magic methods for math operations and operations
# comparison between objects of the Fraction class

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __mul__(self,other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator,new_denominator)
    
    def __add__(self,other):
        a=self.numerator * other.denominator
        b=other.numerator * self.denominator
        new_numerator=a+b
        new_denominator=self.denominator * other.denominator
        return Fraction(new_numerator,new_denominator)
    
    def __sub__(self,other):
        a=self.numerator * other.denominator
        b=other.numerator * self.denominator
        new_numerator=a-b
        new_denominator=self.denominator * other.denominator
        return Fraction(new_numerator,new_denominator)

    def __truediv__(self,other):
        if other.numerator !=0:
            new_numerator=self.numerator * other.denominator
            new_denominator=other.numerator * self.denominator
            return Fraction(new_numerator,new_denominator)
        else:
            print("We can not divizion for 0")

    def __str__(self):
        return f"result {self.numerator}/{self.denominator}"
    

x = Fraction(1, 4)
y = Fraction(0, 2)

print(f"*: {x*y}\n")
print(f"+: {x+y}\n")
print(f"-: {x-y}\n")
print(f"/: {x/y}\n")
