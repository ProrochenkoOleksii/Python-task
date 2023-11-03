#exercise 1

import random
random.randint(1,10)
data = int (input("Input number from 1 to 10:"))
print (random.randint(1,10))
if data==random.randint(1,10):
    print ("You are the winner")
else:
    print ("You are the looser")


#exercise 2
name = input ("Input your name ")
age = int (input ("Input your age "))
age_next = age + 1
print (f"Hello, {name}, on your next birthday you will be {age_next} years")

#exercise 3
import random
string = input ("Input your string:")
result_str = ''.join((random.choice(string)) for i in range(len(string)))
print(result_str)
