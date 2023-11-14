# 1. Напишіть функцію, яка приймає два аргументи (числа) і повертає їх суму.
def my_funct1(n1, n2):
    n3=n1+n2
    return n3

q=my_funct1(5, 10)
print(q)
print ("\n")
# 2. Напишіть функцію, яка приймає ціле число і перевіряє, чи воно парне. 
# Функція повинна повертати True, якщо число парне, і False, якщо непарне.
def my_funct2(k1):
    type(k1)==int
    if k1%2==0:
        return True
    else:
        return False
    
print(my_funct2(189))



# 3. Напишіть функцію, яка приймає список чисел і повертає найбільше з них.

def my_funct3(my_list):
    max_list=max(my_list)
    return max_list

my_list_new=[123,2,4,5,7,0] 
max_new=my_funct3(my_list_new)
print (max_new)

