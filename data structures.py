# Task 1
# Create a program that takes some sentence (string) as input
# and returns a dict containing all unique words as keys and count
# occurrences as value.

my_list = ["car", "apple", "tv", "car", "bus", "bus", "car"]
my_set=set(my_list)

dict_new={key: my_list.count(key) for key in my_set }

print (dict_new)
print ("\n")

#Task 2
# Calculate the total share price, where total price is sum
# price of the product multiplied by the quantity of this particular product.
# The code should return a dictionary with price sums by product type.

stock = {"banana": 6, "apple": 0, "orange": 32, "pear": 15}
prices = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}
final_price={}
for item in stock:
    final_price[item]=stock[item]*prices[item]
print(final_price)
print ("\n")

# Task 3
# List comprehension exercise
# Use list comprehensions to create a containing list
# tuples (i, j) where "i" varies from 1 to 10 and "j" matches
# "i" in a square.

list3={i: i**2 for i in range(1,11)}
print (list3)
print ("\n")


# Task 4
# Create a sheet with the days of the week.
# In one line (well, or as usual) create a dictionary
# of types: {1: "Monday", 2:...
# Also in one line or how to create the reverse
# dictionary {"Monday": 1,..

day_list=["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
dict1={(n+1,day_list[n])for n in range (7)}
dict2={(day_list[n], n) for n in range (7)}

print (dict1)
print ("\n")
print (dict2)
