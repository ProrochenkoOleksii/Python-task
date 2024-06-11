# 1. Phone directory:

# Create a dictionary where keys are people's names and values ​​are their numbers
#phones.
# Add a new contact to the phone book.
# Find phone number by name.

my_dict1 = {"alex": "1234567", "piter": "4657893", "vasyl": "5898026"}
my_dict1.update({"mari": "3009857"})
my_dict1["pavlo"]=6578493
print (my_dict1["alex"])
print ("\n")

# 2. Counting letters:
# Create a dictionary where keys are letters and values ​​are their numbers
# in the line.
# Find the number of specified letters in the given string.
my_dict2={"a": 3, "s": 8, "d": 2, "f": 11}
print (my_dict2["a"])
print ("\n")

# 3. Work with product prices:
# Create a dictionary where the keys are the product names and the values ​​are their prices.
# Find the price of a product by its name.
# Add a new product and its price to the dictionary.
my_dict3={"banan": 23, "tomat": 6, "egg": 17, "cheese": 389}
my_dict3.update({"beer": 20})
print (my_dict3)
print (my_dict3["egg"])
print ("\n")


# 4. Comparison of data:
# Create two dictionaries with names and ages of people.
# Find a person's age by their name.
# Compare data from two dictionaries and create a common dictionary
# with names and ages.
my1={"q": 23, "w": 39, "e": 10, "r": 2}
my2={"a": 53, "s": 59, "d":3, "r": 2}
my1.update(my2)
print (my1)
print ("\n")

# 5. Cost of purchases:
# Create a dictionary with product names and their prices.
# Create a shopping list and calculate the total cost.
my_dict5={"banan": 23, "tomat": 6, "egg": 17, "cheese": 389}
print("banan", "egg")
price=int(my_dict5["banan"])+int(my_dict5["egg"])
print(price)
print ("\n")

#6. Rating of students:
#Create a dictionary with students' names and their grades.
#Find the average score of all students.

class_dict={"q": 10, "w": 8.3, "e": 6.8, "r": 10}
ave_sum=float((class_dict["q"]+class_dict["w"]+class_dict["e"]+class_dict["r"])/4)
print (ave_sum)
print ("\n")

# Tasks on list, set and dict comprehensions
# 1. Generate a simple list of numbers from 1 to 10
list1=[n for n in range(1,11)]
print(list1)
print ("\n")

# 2. Generate a list of squares of numbers from 1 to 10
list2=[n**2 for n in range(1,11)]
print(list2)
print ("\n")

# 3. Generate a list with only even numbers (initial list is a sequence of numbers from 1 to 20)
list3=[n for n in range(1,21) if n%2==0]
print(list3)
print ("\n")


#4. Generate a data collection with filtered unique vowels
# letters in a line (that is, you need to write some line in advance
# text and generate a new sequence based on it)
my_set={"e","r","y","o","j","r","u","i","w","o","a"}
set4={n for n in my_set if n!="r" and n!="w" and n!="j"}
print (set4)
print ("\n")


#5. Generate a dictionary where the keys are numbers from 1 to 5 and the values ​​are their squares.
my_dict5={i: i**2 for i in range (1,6)}
print (my_dict5)
print ("\n")

#6. Create a dictionary based on a list of names where value should contain the length
#(number of letters) of the name.
list_name=["piter", "paul", "johnhy"]
dict6={n: len(list_name[list_name.index(n)]) for n in list_name}
print(dict6)
print ("\n")

#7. Create a dictionary based on two lists - with names and surnames.
#The key can be a first name, and the value can be a last name. Or vice versa.
list_name=["qw", "fg", "th", "re"]
list_surname=["a", "y", "t", "a"]
dict7={key: list_surname[list_name.index(key)] for key in list_name}
print (dict7)
