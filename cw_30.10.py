 
string=input ("Input transaction string ")
if string[0]==";" and string[-1]=="%":
    string = string[1:len(string)-1]
elif string[0]==";":
    string = string[1:len(string)]
elif string[-1]=="%":
    string = string[0:len(string)-1]
print (string)