 
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