# 1. Калькулятор податків:
# Напишіть функцію, яка приймає суму доходу і обчислює загальну суму 
# податку, враховуючи різні ставки податків на прибуток.

# def funct_tax(income):
#     your_tax=0
#     if income<1000:
#         your_tax=income*0.10 # tax 10%
#     elif 1000<=income<10000:
#         your_tax=income*0.17 # tax 17%
#     elif 10000<=income:
#         your_tax=income*0.20 # tax 20%
#     return your_tax

# income_new=int(input("Input your income: "))
# tax_new=funct_tax(income_new)
# print ("Your tax is: ", tax_new)
# print ("\n")   

# 2. Система обліку запасів:
# Створіть функцію, яка дозволяє додавати товари до системи обліку 
# запасів, відстежує кількість товарів та повертає інформацію про 
# наявність товарів на складі.

# 3. Обчислення вартості доставки:
# Напишіть функцію, яка приймає вагу товару та відстань до місця 
# доставки і обчислює вартість доставки згідно з заданими тарифами.

# def del_cost(kg,km):
#     if kg<200 and km<100:
#         total_cost=(0.2*kg+km/100)*2.5
#     elif kg>200 and km<100:
#         total_cost=(0.2*kg+km/100)*3.7
#     else:
#         total_cost=(0.2*kg+km/100)*4.1
#     return total_cost

# kg_new=int(input("Input weight: "))
# km_new=int(input("Input distance: "))
# total_new=int(del_cost(kg_new,km_new))
# print ("Your delivery cost, $: ", total_new)
# print ("\n")


# 4. Система обліку вартості проекту:
# Напишіть функцію, яка приймає вартість робочих годин, кількість годин 
# та додаткові витрати і розраховує загальну вартість проекту.

# def proj_cost(cost_human,hours,other_cost):
#     if cost_human<=10 and hours<=40 and other_cost==0:
#         total_cost=(1.2*cost_human+1.3*hours)*2
#     elif 10<cost_human<20 and 40<hours<50 and 0<other_cost<1000:
#         total_cost=(1.28*cost_human+1.35*hours)*2
#     else:
#         total_cost=(1.18*cost_human+1.2*hours)*3
#     return total_cost

# cost_human_new=int(input("Input cost of working hours: "))
# hours_new=int(input("Input total working hours by week: "))
# other_cost_new=int(input("Input total other cost by the project: "))

# total_cost_new=proj_cost(cost_human_new,hours_new,other_cost_new)
# print ("Your total project cost, $: ", total_cost_new)
# print ("\n")


# 5. Автоматизація операцій з банківським рахунком:
# Створіть функції для переведення грошей між рахунками, перевірки балансу 
# та виведення історії транзакцій.

# 6. Система відстеження завдань:
# Напишіть функції для додавання нових завдань, відзначення завершених та
# виведення списку активних завдань.

# 7. Обчислення середньомісячного обороту:
# Розробіть функцію, яка приймає місячні продажі за останній рік і обчислює 
# середньомісячний оборот.

# def ave_month(mon_sales,mon_cost):
#     sum1=0
#     sum2=0
#     for x in mon_sales:
#         sum1=sum1+int(x)
#     for y in mon_cost:
#         sum2=sum2+int(y)
    
#     print(sum1)
#     print(sum2)
#     mon_price_ave=sum2/len(mon_cost)
#     mon_ave=sum1*mon_price_ave
#     return mon_ave

# my_mon_sales=input("Input your month sales: ")
# my_mon_cost=input("Input price of each product: ")

# k=ave_month(my_mon_sales.split(","),my_mon_cost.split(","))
# print(k)


# 8. Система керування клієнтами:
# Напишіть функції для додавання нових клієнтів, зміни контактної 
# інформації та виведення списку клієнтів.

# def client_new(your_client1):
#     list_client=["s", "eg","kj"]
#     list_client.append(your_client1)
#     return list_client

# def change_cont(your_client2,your_client2_cont):
#     list_client2=["q", "w", "e"]
#     list_cont2=["1223", "234", "2314"]
#     for i in list_client2:
#         if i==your_client2:
#             ind=list_client2.index(i)
#             list_cont2[ind]=your_client2_cont
#         else:
#             pass
#     return list_client2,list_cont2


# your_client2_new=input("Input client for change contact ")
# your_client2_cont_new=input("Input new contact info ")
# m=change_cont(your_client2_new, your_client2_cont_new)
# print(m)


# your_client1_new=input("Input new client ")
# k=client_new(your_client1_new)
# print(k)

# 9. Система відомостей про співробітників:
# Розробіть функції для додавання нових співробітників, зміни їхніх 
# робочих годин та розрахунку зарплати.

# Практика на *args i **kwargs
# 1. Напишіть функцію, яка приймає будь-яку кількість аргументів 
# та повертає їхню суму.
# def my_function(*num):
#     sum=0
#     print(type(num))
#     print(num)
#     for n in num[0]:
#         sum=sum+int(n)
#     return sum

# ar=input("input your numbers ")
# x=my_function(ar.split(","))
# print(x)

# 2. Напишіть функцію, яка приймає будь-яку кількість словників і 
# зливає їх у один.


# 3. Напишіть функцію, яка приймає ключі та значення
# (з використанням **kwargs) та повертає словник з цими парами ключ-значення.
# 4. Напишіть функцію, яка приймає базову зарплату та додаткові 
# параметри (наприклад, бонуси, виплати за додатковий час тощо)
# у вигляді **kwargs та розраховує загальну зарплату.
# 5. Напишіть функцію для розсилки електронних повідомлень, яка 
# приймає адресу електронної пошти та додаткові параметри 
# у вигляді **kwargs (тема, текст повідомлення, прикріплення тощо).