# Task 1
# Largest number
# Write a Python program to get the largest number from a list
# of random numbers of length 10
# Restrictions: use only while loop and random module for
# generation of numbers

from random import randint
list = [randint(1,100) for i in range (10)]
n=0
biggest=0
while n<10:
    if list[n]>biggest:
        biggest=list[n]
        n+=1
    else:
        n+=1
print (list)
print (biggest)
print ("\n")


# Task 2
# Exclusive shared rooms.
# Generate 2 lists of length 10 with random integers
# from 1 to 10 and create a third list containing the common integers
# between 2 initial lists without duplicates.
# Restrictions: use only while loop and random module for
# generation of numbers

from random import randint
list1 = [randint(1,10) for i in range (10)]
list2 = [randint(1,10) for i in range (10)]
list3 = list1 + list2
print (list1)
print (list2)
print (list3)
l=len(list3)
n=1
while n<l:
    if list3[n]==list3[n-1]:
        list3.pop(n)
        print (list3)
        n+=1
    else:
        n+=1
print (list3)
print ("\n")

# Task 3
# Extract numbers.
# Create a list that contains all integers from 1 to 100,
# then find all integers divisible by 7 from the list
# but not multiples of 5, and store them in a separate list. Finally,
# print the list.
# Restrictions: only use a while loop for iteration

my_list=[*range(1,101)]
my_list_new=[]
i=0
while i<100:
    if my_list[i]%7==0 and my_list[i]%5!=0:
        my_list_new.append(my_list[i])
        i+=1
    else:
        i+=1
print (my_list_new)
