# Завдання 1
# Напишіть функцію під назвою oops, яка під час виклику явно викликає 
# виключення IndexError. Потім напишіть іншу функцію, яка викликає oops у 
# операторі try/except, щоб виявити помилку. Що станеться, якщо ви зміните 
# oops на виклик KeyError замість IndexError?
def oops(list1):
    try:
        n=list1[len(list1)+1]
    except IndexError:
        print ("Out of range")

my_list=[1, 2, 3, 4]
k=oops(my_list)

def oops2(list2):
    try:
        oops(list2)
    except IndexError:
        print("Wrong")

my_list2=[1, 2, 3, 4]
k=oops2(my_list2)

# Завдання 2
# Напишіть функцію, яка приймає два числа від користувача за допомогою 
# input(), викликає числа a і b , а потім повертає значення квадрата a ,
# поділеного на b , створює блок try-except, який викликає виняток, якщо 
# задано два значення функцією введення не були числа, а якщо значення b 
# дорівнювало нулю (не можна ділити на нуль).    

def my_fun(a,b):
    try:
        c=a*a/b
        print(f"Result: {c}")
    except ZeroDivisionError:
        print("num is ZERO!")
    except ValueError:
        print("wrong TYPE!")
a=int(input("input 1 num: "))
b=int(input("input 2 num: "))
n=my_fun(a,b)



    


