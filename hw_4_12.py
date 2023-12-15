# Завдання 1

# Перевантаження методу.

# Створіть базовий клас під назвою Animal із методом під назвою talk,
# а потім створіть два підкласи: Dog і Cat і зробіть їх власну реалізацію
# методу talk іншою. Наприклад, собака може друкувати «гав гав»,
# а котяча — «мяу».

# Крім того, створіть просту загальну функцію, яка приймає як вхідний 
# екземпляр класів Cat або Dog і виконує метод talk для вхідного параметра.  

# class Animal():
#     def __init__(self,animal):
#         self.animal = animal
    
#     def talk(self):
#         if animal=="Dog":
#             return f"{self.animal} say: 'gav-gav'"
#         elif animal=="Cat":
#             return f"{self.animal} say: 'myau-myau'"
#         else:
#             return f"{self.animal} can not speak :-)"



# class Dog(Animal):
#     def __init__(self,type):
#         self.type = type

#     def talk(self):
#         return f"{self.type} say: 'gav-gav'"


# class Cat(Animal):
#     def __init__(self,type):
#         self.type = type

#     def talk(self):
#         return f"{self.type} say: 'myau-myau'"

# animal=Animal("Bird")
# dog1=Dog("My dog")
# cat1=Cat("My cat")
# print(cat1.talk())
# print(dog1.talk())
# print(animal.talk())


# Завдання 2

# Бібліотека
# Напишіть структуру класу, яка реалізує бібліотеку. Класи:
# 1) Бібліотека - назва, книги = [], автори = []
# 2) Книга – назва, рік, автор (автор має бути екземпляром класу Author)
# 3) Автор - ім'я, країна, день народження, книги = []

# Бібліотечний клас
# Методи:
# - new_book(name: str, year: int, author: Author) - повертає екземпляр
# класу Book і додає книгу до списку книг для поточної бібліотеки.
# - group_by_author(автор: Автор) - повертає список усіх книг, згрупованих
# за вказаним автором
# - group_by_year(year: int) - повертає список усіх книг, згрупованих за
# вказаним роком

# Усі 3 класи повинні мати читабельні методи __repr__ і __str__.
# Крім того, клас книги повинен мати змінну класу, яка містить кількість
# усіх існуючих книг

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

# Завдання 3
# дріб
# Створіть клас  Fraction , який буде представляти всю базову арифметичну
# логіку для дробів (+, -, /, *) з належною перевіркою й обробкою помилок. 
# Потрібно додати магічні методи для математичних операцій та операцій
# порівняння між об’єктами класу Fraction

# class Fraction:
#     def __init__(self, numerator, denominator):
#         self.numerator = numerator
#         self.denominator = denominator

#     def __mul__(self,other):
#         new_numerator = self.numerator * other.numerator
#         new_denominator = self.denominator * other.denominator
#         return Fraction(new_numerator,new_denominator)
    
#     def __add__(self,other):
#         a=self.numerator * other.denominator
#         b=other.numerator * self.denominator
#         new_numerator=a+b
#         new_denominator=self.denominator * other.denominator
#         return Fraction(new_numerator,new_denominator)
    
#     def __sub__(self,other):
#         a=self.numerator * other.denominator
#         b=other.numerator * self.denominator
#         new_numerator=a-b
#         new_denominator=self.denominator * other.denominator
#         return Fraction(new_numerator,new_denominator)

#     def __truediv__(self,other):
#         if other.numerator !=0:
#             new_numerator=self.numerator * other.denominator
#             new_denominator=other.numerator * self.denominator
#             return Fraction(new_numerator,new_denominator)
#         else:
#             print("We can not divizion for 0")

#     def __str__(self):
#         return f"result {self.numerator}/{self.denominator}"
    

# x = Fraction(1, 4)
# y = Fraction(0, 2)

# print(f"*: {x*y}\n")
# print(f"+: {x+y}\n")
# print(f"-: {x-y}\n")
# print(f"/: {x/y}\n")