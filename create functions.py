# Task 1
# Simple function.
# Create a simple function called favorite_movie that accepts a string from
# with the name of your favorite movie. Then the function should output
# "My favorite movie is called {name}."
def favourite_movie (name):
    
    print("My favourite movie is: " + name)

favourite_movie ("matrix")
print ("\n")

# Task 2
# Creating a dictionary.
# Create a function called make_country that accepts a name and a capital
# countries as parameters. Then create a dictionary from these two,
# using "name" as key and "capital" as parameter.
# Make the function output the dictionary value to make sure it
# works properly.
def make_country(name, capital):
    my_dict=dict()
    my_dict.update({name: capital})
    print (my_dict)
a=input("input name of country: ")
b=input("input capital: ")
make_country(a,b)
 

#Task 3
# Simple calculator.
# Create a function called make_operation that takes a simple
# arithmetic operator as the first parameter (for simplicity let it
# will only be "+", "-" or "*") and any number of arguments (numbers only)
# as the second parameter. Then returns the sum or product of all numbers in an arbitrary
# parameters. Example:
# call make_operation('+', 7, 7, 2) should return 16
# call make_operation('-', 5, 5, -10, -20) should return 30
# call make_operation('*', 7, 6) should return 42

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
    
