name = "Oleksandr"
surname = "Makedonskii"
company = "@kobzar.com"
email_1 = name[0:4]+surname[0:3]+company
print(email_1)
email_2 = name[0]+'.'+surname+company
print(email_2)
email_3 = name[0:9:2]+'.'+surname[0:11:2]+company
print(email_3)