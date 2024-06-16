# Task 1
# Write a function called oops that explicitly calls when called
# throw IndexError. Then write another function that calls oops in
# try/except statements to catch the error. What happens if you change
# oops on calling KeyError instead of IndexError?
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

# Task 2
# Write a function that accepts two numbers from the user using
# input(), calls the numbers a and b , and then returns the value of the square of a ,
# divided by b , creates a try-except block that throws an exception if
# given two values ​​by the input function were not numbers, and if the value b
# was equal to zero (not divisible by zero).

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



    


