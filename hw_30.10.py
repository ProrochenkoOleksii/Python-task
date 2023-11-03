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