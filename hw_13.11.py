# Завдання 1
# Напишіть функцію під назвою oops, яка під час виклику явно викликає 
# виключення IndexError. Потім напишіть іншу функцію, яка викликає oops у 
# операторі try/except, щоб виявити помилку. Що станеться, якщо ви зміните 
# oops на виклик KeyError замість IndexError?
# def oops(list1):
#     n=list1[len(list1)+1]
#     print (n)

# my_list=[1, 2, 3, 4]
# k=oops(my_list)

# def oops2(list2):
#     try:
#         oops(list2)
#     except KeyError:
#         print("Wrong")

 

# Завдання 2
# Напишіть функцію, яка приймає два числа від користувача за допомогою 
# input(), викликає числа a і b , а потім повертає значення квадрата a ,
# поділеного на b , створює блок try-except, який викликає виняток, якщо 
# задано два значення функцією введення не були числа, а якщо значення b 
# дорівнювало нулю (не можна ділити на нуль).    

def my_fun(a,b):
    
    if type(a)==str and type(b)==str:
        try:
            c=a*a/b
        except:
            print("wrong Type")
    try:
        b==0
    except ZeroDivisionError:
        print ("num is ZERO!!!")
    
    c=a*a/b
    return c


a=int(input("input 1 num: "))
b=int(input("input 2 num: "))
k=my_fun(a,b)
print(k)
    


