 
string=str(input ("Input transaction string "))
if string[0]==";" and string[-1]=="%":
    string = string[1:len(string)-1]
elif string[0]==";":
    string = string[1:len(string)]
elif string[-1]=="%":
    string = string[0:len(string)-1]
print (string)

string_new=input ("Input transaction string ")
string_last=" "
for i in string_last:
    if i=="&":
        pass
    else:
        string_last+=i
print (string_last)

money=int(input("how much money per month? "))
age=int(input("your age "))
job=input("do you have a job?")
if money>100 and age>18 and job=="yes":
    print ("Congratulations! Money are your.")
elif money>1000 and age>20 and job=="no":
    print ("Congratulations! Money are your.")
else:
    print ("Without money")


# 1. Write a function that takes two arguments (numbers) and returns their sum.
def my_funct1(n1, n2):
    n3=n1+n2
    return n3

q=my_funct1(5, 10)
print(q)
print ("\n")

# 2. Write a function that takes an integer and checks if it is even.
# The function should return True if the number is even, and False if it is odd.
def my_funct2(k1):
    type(k1)==int
    if k1%2==0:
        return True
    else:
        return False
    
print(my_funct2(189))


# 3. Write a function that takes a list of numbers and returns the largest of them.
def my_funct3(my_list):
    max_list=max(my_list)
    return max_list

my_list_new=[123,2,4,5,7,0] 
max_new=my_funct3(my_list_new)
print (max_new)

# 4. Tax calculator:
# Write a function that takes an income amount and calculates the total amount
# of tax, taking into account different rates of income taxes.

def funct_tax(income):
    your_tax=0
    if income<1000:
        your_tax=income*0.10 # tax 10%
    elif 1000<=income<10000:
        your_tax=income*0.17 # tax 17%
    elif 10000<=income:
        your_tax=income*0.20 # tax 20%
    return your_tax

income_new=int(input("Input your income: "))
tax_new=funct_tax(income_new)
print ("Your tax is: ", tax_new)
print ("\n")   


# 5. Calculation of the cost of delivery:
# Write a function that takes the weight of the item and the distance to the location
# of deliveries and calculates the cost of delivery according to the specified tariffs.

def del_cost(kg,km):
    if kg<200 and km<100:
        total_cost=(0.2*kg+km/100)*2.5
    elif kg>200 and km<100:
        total_cost=(0.2*kg+km/100)*3.7
    else:
        total_cost=(0.2*kg+km/100)*4.1
    return total_cost

kg_new=int(input("Input weight: "))
km_new=int(input("Input distance: "))
total_new=int(del_cost(kg_new,km_new))
print ("Your delivery cost, $: ", total_new)
print ("\n")


# 6.Project cost accounting system:
# Write a function that takes the value of working hours, the number of hours
# and additional costs and calculates the total cost of the project.

def proj_cost(cost_human,hours,other_cost):
    if cost_human<=10 and hours<=40 and other_cost==0:
        total_cost=(1.2*cost_human+1.3*hours)*2
    elif 10<cost_human<20 and 40<hours<50 and 0<other_cost<1000:
        total_cost=(1.28*cost_human+1.35*hours)*2
    else:
        total_cost=(1.18*cost_human+1.2*hours)*3
    return total_cost

cost_human_new=int(input("Input cost of working hours: "))
hours_new=int(input("Input total working hours by week: "))
other_cost_new=int(input("Input total other cost by the project: "))

total_cost_new=proj_cost(cost_human_new,hours_new,other_cost_new)
print ("Your total project cost, $: ", total_cost_new)
print ("\n")


# 7. Calculation of the average monthly turnover:
# Develop a function that takes monthly sales for the last year and calculates
# average monthly turnover.

def ave_month(mon_sales,mon_cost):
    sum1=0
    sum2=0
    for x in mon_sales:
        sum1=sum1+int(x)
    for y in mon_cost:
        sum2=sum2+int(y)
    
    print(sum1)
    print(sum2)
    mon_price_ave=sum2/len(mon_cost)
    mon_ave=sum1*mon_price_ave
    return mon_ave

my_mon_sales=input("Input your month sales: ")
my_mon_cost=input("Input price of each product: ")

k=ave_month(my_mon_sales.split(","),my_mon_cost.split(","))
print(k)


# 8. Customer management system:
# Write functions for adding new customers, changing contact information
# information and output of the list of customers.

def client_new(your_client1):
    list_client=["s", "eg","kj"]
    list_client.append(your_client1)
    return list_client

def change_cont(your_client2,your_client2_cont):
    list_client2=["q", "w", "e"]
    list_cont2=["1223", "234", "2314"]
    for i in list_client2:
        if i==your_client2:
            ind=list_client2.index(i)
            list_cont2[ind]=your_client2_cont
        else:
            pass
    return list_client2,list_cont2

your_client2_new=input("Input client for change contact ")
your_client2_cont_new=input("Input new contact info ")
m=change_cont(your_client2_new, your_client2_cont_new)
print(m)

your_client1_new=input("Input new client ")
k=client_new(your_client1_new)
print(k)

# 9.Write a function that accepts any number of arguments
# and returns their sum.
def my_function(*num):
    sum=0
    print(type(num))
    print(num)
    for n in num[0]:
        sum=sum+int(n)
    return sum

ar=input("input your numbers ")
x=my_function(ar.split(","))
print(x)
