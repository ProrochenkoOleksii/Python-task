# Завдання 1
# Створіть програму, яка має деяке речення (рядок) на вхідних даних 
# і повертає dict, що містить усі унікальні слова як ключі та кількість 
# входжень як значення. 

my_list = ["car", "apple", "tv", "car", "bus", "bus", "car"]
my_set=set(my_list)

dict_new={key: my_list.count(key) for key in my_set }

print (dict_new)
print ("\n")

# Завдання 2
# Обчисліть загальну ціну акцій, де загальна ціна є сумою
# ціни товару, помноженої на кількість саме цього товару.
# Код повинен повертати словник із сумами цін за типами товарів.
stock = {"banana": 6, "apple": 0, "orange": 32, "pear": 15}
prices = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}
final_price={}
for item in stock:
    final_price[item]=stock[item]*prices[item]
print(final_price)
print ("\n")

# Завдання 3
# Вправа на розуміння списку
# Використовуйте розуміння списку, щоб створити список, що містить 
# кортежі (i, j), де «i» змінюється від 1 до 10, а «j» відповідає
# «i» у квадраті.
list3={i: i**2 for i in range(1,11)}
print (list3)
print ("\n")




# Завдання 4
# Створити лист із днями тижня.
# В один рядок (ну або як завжди) створіть словник
# виду: {1: "Понеділок", 2:...
# Також в один рядок або як вдасться створити зворотний 
# словник {"Понеділок": 1,..

day_list=["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
dict1={(n+1,day_list[n])for n in range (7)}
dict2={(day_list[n], n) for n in range (7)}

print (dict1)
print ("\n")
print (dict2)