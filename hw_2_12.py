# Завдання 1

# Школа

# Створіть структуру класу на Python, яка представлятиме людей у ​​школі. 
# Створіть базовий клас під назвою Person, клас під назвою Student і ще один 
# під назвою Teacher. Спробуйте знайти якомога більше методів і атрибутів,
# які належать до різних класів, і майте на увазі, які з них є загальними,
# а які ні. Наприклад, ім’я має бути атрибутом Person, тоді як зарплата має 
# бути доступна лише вчителю. 

# class Person:
#     def __init__(self, name, science):
#         self.name = name
#         self.science = science


# class Student(Person):
#     def __init__ (self, name, science, groupe, age):
#         super().__init__(name, science)
#         self.science = science
#         self.groupe = groupe
#         self.age = age

#     def print_info(self):
#         attributes = vars(self)
#         print("This is student's info: ")
#         for attribute, value in attributes.items():
#             print (f'{attribute}: {value}')


# class Teacher(Person):
#     def __init__(self, name, science, experience, salary_year):
#         super().__init__(name, science)
#         self.science = science
#         self.experience = experience
#         self.salary_year = salary_year

#     def print_info(self):
#         attributes = vars(self)
#         print("This is teacher's info: ")
#         for attribute, value in attributes.items():
#             print (f'{attribute}: {value}')

# student1=Student("john", "math", 3456, 18)
# student2=Student("peter", "biology", 2059, 19)

# teacher1=Teacher("kris", "math", 12, 11000)
# teacher2=Teacher("james", "filology", 20, 23000)

# student1.print_info()
# teacher2.print_info()


# Завдання 2

# Математик

# Реалізуйте клас Mathematician, який є допоміжним класом для виконання
# математичних операцій зі списками
# Клас не приймає жодних атрибутів і має лише методи:

# square_nums (бере список цілих чисел і повертає список квадратів)
# remove_positives (бере список цілих чисел і повертає його без додатних чисел
# filter_leaps (бере список дат (цілі числа) і видаляє ті, які не
# є «високосними роками»


# class Mathematician ():

#     def square_nums(self, my_list1):
#         new_list=list()
#         for elements in my_list1:
#             elements_new=elements**2
#             new_list.append(elements_new)
#         return new_list
    
#     def remove_positives(self, my_list2):
#         new_list=list()
#         for elements in my_list2:
#             if elements<0:
#                 new_list.append(elements)
#             else:
#                 pass
#         return new_list
    
#     def filter_leaps(self, my_list3):
#         new_list=list()
#         for elements in my_list3:
#             if (elements % 4 == 0 and elements % 100 != 0) or elements % 400 == 0:
#                 new_list.append(elements)
#             else:
#                 pass
#         return new_list

# m = Mathematician()
# my_list1=[7, 11, 5, 4]
# print(m.square_nums(my_list1))

# my_list2=[26, -11, -8, 13, -90]
# print(m.remove_positives(my_list2))

# my_list3=[2001, 1884, 1995, 2003, 2020]
# print(m.filter_leaps(my_list3))


# Завдання 3
# Магазин товарів
# Напишіть клас Product, який має три атрибути:

# типу
# назва
# ціна
# Потім створіть клас ProductStore, який матиме кілька продуктів і 
# працюватиме з усіма продуктами в магазині. Усі методи, якщо вони не можуть 
# виконати свою дію, повинні викликати ValueError з відповідною інформацією 
# про помилку.

# Підказки. Використовуйте концепції агрегації/композиції під час реалізації
#  класу ProductStore. Ви також можете реалізувати додаткові класи для роботи 
# з певним типом товару тощо.

# Крім того, клас ProductStore повинен мати такі методи:

# add(product, кількість) - додає визначену кількість одного продукту з попередньо
#  визначеною надбавкою до ціни для вашого магазину (30 відсотків)
# set_discount(identifier, percent, identifier_type='name') - додає знижку
#  на всі товари, зазначені введеними ідентифікаторами (тип або назва).
#  Знижка повинна бути вказана у відсотках
# sell_product(product_name, сума) - видаляє певну кількість товарів із
#  магазину, якщо вони є, в іншому випадку викликає помилку. Він також
#  збільшує дохід, якщо метод sell_product завершується успішно.
# get_income() - повертає суму багатьох, зароблених екземпляром ProductStore.
# get_all_products() - повертає інформацію про всі наявні товари в магазині.
# get_product_info(product_name) - повертає кортеж із назвою товару та
#  кількістю товарів у магазині.

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


# Завдання 4

# Спеціальний виняток

# Створіть власний виняток під назвою «CustomException», який можна
#  успадкувати від базового класу Exception, але розширити його
# функціональність, щоб реєструвати кожне повідомлення про помилку
# у файлі під назвою «logs.txt». Поради: використовуйте метод __init__,
# щоб розширити функціональні можливості для збереження повідомлень у файл

# class Exception():
#     def __init__(self,msg):
#         self.message = msg

# class CustomException(Exception):
    
#     def __init__(self,msg):
#         super().__init__(msg)
#         self.msg = msg

#     def my_log(self):
#         with open ("file_practice/logs.txt", "w") as myfile:
#             myfile.write(f"{self.msg}")    

# msg = "message about exception"

# try:
#     raise CustomException()

# except Exception:  
#     print("my exception")

