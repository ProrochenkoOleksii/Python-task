# Task 1
# Files
# Write a script that creates a new output file named myfile.txt and
# writes the string "Hello file world!" in this. Then write another script,
# which opens myfile.txt, reads and prints its contents. Run two
# scripts from the system command line.

my_line="Hello file world!"
with open ("file_practice/myfile.txt", "w") as mf:
    mf.write(my_line)
    
with open ("file_practice/myfile.txt", "r") as mf:
    my_file=mf.read()
    print(my_file)



# Task 2
# Expand the Phone Book application
# Functionality of the Phone book program:
# Add new entries
# Search by name
# Search by last name
# Search by last name
# Search by phone number
# Search by city or state
# Delete the entry for this phone number
# Update the record for the specified phone number
# Ability to exit the program

# The first argument of the program must be the name of the phone book. Program
# should load the JSON data if it is present in the program folder,
# otherwise an error will occur. After the user exits, all data should be
# stored in the downloaded JSON.

phone_book=[{"1st name": "alex",
             "2nd name": "green",
             "full name": "alex green",
             "phone number": 1234567,
             "city or state": "Rome"},
             {"1st name": "john",
             "2nd name": "smith",
             "full name": "john smith",
             "phone number": 2345678,
             "city or state": "Madrid"}]

import json
with open ("file_practice/phone_book.json", "w") as pb:
    json.dump(phone_book,pb)

with open ("file_practice/phone_book.json", "r") as pb:
    data=json.load(pb)
    your_name=input("Choose your name (john V alex): ")
    for n in data:
        for key, value in n.items():
            if value==your_name:
                print(n)
        
