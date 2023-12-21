# Завдання 1

# Створіть метод класу під назвою `validate`, який слід викликати з 
# методу `__init__` для перевірки електронної пошти параметра, 
# переданого конструктору. Логіка всередині методу `validate` може полягати 
# в тому, щоб перевірити, чи переданий параметр електронної пошти є дійсним 
# рядком електронної пошти.

# Підтвердження електронної пошти:

# Дійсний формат електронної адреси 

# Адреса електронної пошти 

# class MyClass:
#     def __init__(self, email):
#         self.email = email
        
#     def validate(self):
#         if "@" in self.email:
#             if self.email[-1]=="@":
#                 print("Wrong email address!")
#             elif self.email[0]=="@":
#                 print("Wrong email address!")
#             else:
#                 return "Emil address is validate"
#         else:
#             print("Wrong email address!")

# em = MyClass("@gmail.com")
# print(em.validate())        


# Завдання 2

# Реалізуйте 2 класи, перший — Бос, а другий — Робочий.
# Worker має властивість 'boss', і його значення має бути екземпляром Boss.
# Ви можете перепризначити це значення, але вам слід перевірити, чи нове 
# значення є Boss. У кожного боса є список своїх працівників. 
# Ви повинні реалізувати метод, який дозволяє додавати працівників до боса. 
# Ви не маєте права додавати екземпляри класу Boss до списку працівників 
# безпосередньо через доступ до атрибута, натомість використовуйте геттери 
# та сетери!
# Ви можете змінити існуючий код.
# id_ - це просто випадкове унікальне ціле число

 
# class Boss:
#     def __init__(self, id_: int, name: str, company: str):
#         self.id_ = id_
#         self.name = name
#         self.company = company
#         self.workers = []

#     def new_worker(self,id_,name,company,boss):
#         workers = Worker(id_=id_,name=name,company=company,boss=boss)
#         self.workers.append(workers)
#         return workers  
    
#     def __str__(self):
#         workers_info = "\n".join(str(worker) for worker in self.workers)
#         return f"Information about your workers: {workers_info}"
    
# class Worker:
#     def __init__(self, id_: int, name: str, company: str, boss: Boss):
#         self.id_ = id_
#         self.name = name
#         self.company = company
#         self.boss = boss

#     def __str__(self):
#         return f"\n Worker with # {self.id_} {self.name} from company: {self.company}"

      

# boss1=Boss(2635,"John","KPMG")
# boss2=Boss(26005,"Kris","OKKO")

# boss2.new_worker(5106,"Serg","OKKO",boss2)

# boss1.new_worker(5786,"Ivan","Coca-cola",boss1)
# boss1.new_worker(658,"Peter","KPMG",boss1)

# print(boss1.__str__())
# print(boss2.__str__())


# 1. Клас для обчислення площі прямокутника:
# Створіть клас Rectangle, який має атрибути для зберігання довжини та 
# ширини прямокутника. Використовуйте декоратор @property для повернення
# площі прямокутника.

# class Rectangle():
#     def __init__(self,lenght,width):
#         self.lenght = lenght
#         self.width = width

#     @property
#     def square(self):
#         return self.lenght*self.width
    
#     def __str__(self):
#         return f"Square is: {self.square}"
        
# a=Rectangle(2,6)
# print(a)