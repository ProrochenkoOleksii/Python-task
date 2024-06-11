#Tasks for the for loop:

#1. Print all the odd numbers in the interval from 1 to 20 using
# of the for loop.

for n in range (1, 21):
    if n%2!=0:
        print (n)
print ("\n")

#2. Create a list of numbers and find the sum of all elements in the list by
#using the for loop.
sum=0
my_list2 = [2, 13, 4, 5, 6]
for n in my_list2:
    sum=sum+n
print(sum)
print ("\n")


#3. Create a list of words and output words that contain more than 5 letters,
#using a for loop.

my_list3 = ["qwerty", "qwertyu", "qw", "qwer"]
for i in my_list3:
    if len(i)>5:
        print (i)
print ("\n")


#4. Create a list that contains the numbers 1 to 10. Print all the numbers
#except the number 3, using a for loop.

my_list4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for n in my_list4:
    if n!=3:
        print (n)
print ("\n")


# 5. Create a list from different data types (numbers, strings, boolean values)
# and output the type of each element using a for loop.

my_list5 = ["dkhf", 1, 4, False, "sdlfnd", True]
for n in my_list5:
    print (type(n))
print ("\n")

# Tasks for the while loop:
#1. Using a while loop, output all even numbers in
#intervals from 1 to 20.

list1 = [*range(1, 21)]
n=1
while n<len(list1):
    if n%2==0:
        print (n)
        n+=1
    else:
        n+=1
print ("\n")


#2. Create a variable "sum" and add numbers from 1 to 10 to it
#using a while loop. Print the received sum.

sum=0
n=1
while n<=10:
    sum=sum+n
    n+=1
print (sum)
print ("\n")

# 3. Create a variable "counter" (counter) and use a while loop,
# to count the number of numbers that are divisible by 5 in the interval
# from 1 to 100.

counter = 0
n=0
list3=[*range(0,100)]
while n<len(list3):
    if list3[n]%5==0:
        counter+=1
        n+=1
    elif list3[n]%5!=0:
        n+=1
print (counter)
print ("\n")    


# 4. Ask the user for a password. Use a while loop to
# keep asking for password until it enters the correct password.

parol = "qwerty"
parol_user = str(input ("Input your password"))
while parol_user!=parol:
    parol_user=str(input ("Input your password"))
print ("Password is wright")
print ("\n")

# 5. Create a list of numbers and output its elements using
# while loop.

list5=[*range(1,10)]
n=0
while n<len(list5):
    print(list5[n])
    n+=1
print("\n")

# exercise1
string = "hello world"
lenght = len(string)
string_new = string[0:2] + string[lenght-2:lenght]
print (string_new)

string_1 = "my"
lenght_1 = len(string_1)
string_neww = string_1[0:2] + string_1[lenght_1-2:lenght_1]
print (string_neww)

string_2 = "x"
if len(string_2)<2:
    print("Empty String")
else:
    pass

# exercise2
num = "4638495736"
l = len(num)
if l <= 10:
    print (f"Phone number {num} is TRUE")
else:
    print (f"Phone number {num} is FALSE")

#exercise3
x=21+35-17
ans = input ("Answer is:")
if ans != 39:
    print ("You are loose")
else:
    print ("You are wright")


#exercise4
name = "oleksii"
name_new = input ("input your name:")
name_new_d=str.casefold (name_new)
if name == name_new_d:
    print ("TRUE")
else:
    print ("FALSE")



# Tasks on data structures in Python:

# 1. Create a list containing your favorite colors.
# Print the first and last elements of the list.

list_color=["red", "green", "brown", "black"]
print (list_color[0])
print (list_color[-1])
print ("\n")

# 2. Create a tuple that contains the names of the months of the year.
# Try changing one of the elements of the tuple and make sure that
# get an error.

tuple_month=("jan", "feb", "mar", "apr", "may", "june")
tuple_month.append("july")
print (tuple_month)


# 3. Create two sets that contain numbers from 1 to 10 and
# from 5 to 15 respectively. Derive their union, intersection and difference.

set1 = {1, 2, 3 , 4, 5, 6, 7, 8, 9, 10}
set2 = {5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
print (set1.union(set2))
print (set2.intersection(set1))
print (set1.difference(set2))
print (set2.difference(set1))
print ("\n")

# 4. Create a list containing several names and surnames.
# Sort the list alphabetically and display its sorted version.

list_name = {"alex", "piter", "jack", "john", "mari"}
print (list_name)
print (sorted (list_name))

# 5. Create a set that contains even numbers from 1 to 20.
# Create another set that contains numbers that are divisible by 3.
# Print the union of both sets.

set51={2,4,6,8,10,12,14,16,18,20}
set52={3,6,9,12,15,18}
print (set51.union(set52))

# 6. Create a tuple that contains different data types such as numbers,
# strings and boolean values.
my_tuple = (1, 3, True, "jsdhfgsj", 7)
print (my_tuple)

# 7. Create a list of numbers and output the sum of all the numbers in the list.
list71 = [1,5,123,3,7,9,89]
print (sum(list71))

# 8. Create a tuple containing different items
# (eg fruit, books, toys). Output the fifth element of the tuple.
my_tuple81=("ball", "book", "toy", 4567, "A", 4, "sdjkhf")
print (my_tuple81[5])


# 9. Create a list of words. Elicit all the words that have
# more than 5 letters.
list91=["asdljfhldfhlkjg", "Ahgsdhgkfh", "sd", "sd34fjblj", "q"]
for n in list91:
    if len(n)>5:
        print (n)

# 10. Create a list of students (tuples with name and average score).
# Find the student with the highest GPA and display his name.
stud=("alex", 4.6, "john", 5.8, "jack", 7.3)
studhigh = int()
for n in stud:
    if type (n) != str:
        if n > studhigh:
            studhigh = i
        else:
            pass
    else:
        pass
print (studhigh)


# 11. Create a list of orders (tuples that contain the order number
#that amount). Find the total amount of all orders and display it.

order_1 = (234, 84)
order_2 = (231, 38)
order_3 = (230, 76)
sum=0

order_list = {order_1, order_2, order_3}
for i in order_list:
    sum=sum+i[-1]
print (sum)

# 12. Create a list of tuples with data about site visitors
# (IP address and time of visit). Find the most popular time of day,
# when the site is visited the most. Implement a function to count
# of the total number of visits to the site. Display the total number
# of visits
visitor_1 = (236457, "m")
visitor_2 = (234556, "d")
visitor_3 = (123456, "e")
visitor_4 = (374836, "d")
count_m=0
count_d=0
count_e=0

visit_list = [visitor_1, visitor_2, visitor_3, visitor_4]
for i in visit_list:
    if i[-1]=="m":
        count_m+=1
    elif i[-1]=="d":
        count_d+=1
    elif i[-1]=="e":
        count_e+=1
print ("morning:", count_m, "day:",count_d, ",evening:",count_e)
print (f""all orders:", {count_m+count_d+count_e}")


# 13. Create a list of tuples where each tuple contains the product name
# that price. Calculate the total cost of goods including tax
# and bring her out.

goods_1 = ("banan", 123)
goods_2 = ("auto", 34)
goods_3 = ("phone", 128.4)
goods_4 = ("apple", 21.5)
tax = 1.2
sum=0

goods_list = [goods_1, goods_2, goods_3, goods_4]
for i in goods_list:
    i[-1]=i[-1]*tax
    sum+=i[-1]
    print (sum)
