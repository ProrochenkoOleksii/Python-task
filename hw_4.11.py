# Завдання 1
# Найбільше число
# Напишіть програму на Python, щоб отримати найбільше число зі списку 
# випадкових чисел довжиною 10
# Обмеження: використовуйте лише цикл while і випадковий модуль для 
# генерації чисел
# from random import randint
# list = [randint(1,100) for i in range (10)]
# n=0
# biggest=0
# while n<10:
#     if list[n]>biggest:
#         biggest=list[n]
#         n+=1
#     else:
#         n+=1
# print (list)
# print (biggest)


# Завдання 2
# Ексклюзивні загальні номери.
# Згенеруйте 2 списки довжиною 10 із випадковими цілими числами 
# від 1 до 10 і створіть третій список, що містить загальні цілі числа 
# між 2 початковими списками без дублікатів.
# Обмеження: використовуйте лише цикл while і випадковий модуль для 
# генерації чисел
from random import randint
list1 = [randint(1,10) for i in range (10)]
list2 = [randint(1,10) for i in range (10)]
list3 = list1 + list2
print (list1)
print (list2)
print (list3)
l=len(list3)
print (l)
n=1
while n<l:
    if list3[n-1]==list3[n]:
        list3.pop(n)
        print (list3)
        n+=1
    else:
        n+=1
    print (list3)

# Завдання 3
# Витяг чисел.
# Створіть список, який містить усі цілі числа від 1 до 100, 
# потім знайдіть зі списку всі цілі числа, які діляться на 7, 
# але не кратні 5, і збережіть їх в окремому списку. Нарешті, 
# роздрукуйте список.
# Обмеження: використовуйте лише цикл while для ітерації

# my_list=[*range(1,101)]
# my_list_new=[]
# i=0
# while i<100:
#     if my_list[i]%7==0 and my_list[i]%5!=0:
#         my_list_new.append(my_list[i])
#         i+=1
#     else:
#         i+=1
# print (my_list_new)