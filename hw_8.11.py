# Завдання 1
# Проста функція.
# Створіть просту функцію під назвою favorite_movie, яка приймає рядок із
# назвою вашого улюбленого фільму. Потім функція повинна вивести
# «Мій улюблений фільм називається {name}».
def favourite_movie (name):
    
    print("My favourite movie is: " + name)

favourite_movie ("matrix")
print ("\n")


# Завдання 2
# Створення словника.
# Створіть функцію під назвою make_country, яка приймає назву та столицю 
# країни як параметри. Потім створіть словник із цих двох, 
# використовуючи «name» як ключ і «capital» як параметр. 
# Змусьте функцію вивести значення словника, щоб переконатися, що вона 
# працює належним чином.
# def make_country(name, capital):
#     my_dict=dict([(key, value) for key in name for value is capital])
#     print (my_dict)

# make_country("ukraine", "kyiv")
 

# Завдання 3
# Простий калькулятор.
# Створіть функцію під назвою make_operation, яка приймає простий
# арифметичний оператор як перший параметр (для спрощення нехай це 
# буде лише «+», «-» або «*») і довільну кількість аргументів (тільки чисел)
#  як другий параметр. Потім повертає суму або добуток усіх чисел у довільному
#    параметрі. Наприклад:

# виклик make_operation('+', 7, 7, 2) має повернути 16
# виклик make_operation('-', 5, 5, -10, -20) має повернути 30
# виклик make_operation('*', 7, 6) має повернути 42  
def make_operation(sign, points):
    my_sum=0
    my_sub=0
    my_mult=1
    if sign == "+":
        for x in points:
            my_sum=my_sum+x
        return my_sum
    elif sign == "-":
        for x in points:
            my_sub=x-my_sub
        return my_sub
    elif sign == "*":
        for x in points:
            my_mult=my_mult*x
        return my_mult
            

points1=[7,7,2]
l=make_operation("+", points1)
points2=[5,5,-10,-20]     
q=make_operation("-", points2)
points3=[7,6]
k=make_operation("*", points3)
print(l, "\n", q, "\n", k)
    