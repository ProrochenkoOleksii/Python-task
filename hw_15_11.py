# Завдання 1
# Файли
# Напишіть сценарій, який створює новий вихідний файл під назвою myfile.txt і 
# записує рядок "Hello file world!" в цьому. Потім напишіть інший сценарій, 
# який відкриває myfile.txt, читає та друкує його вміст. Запустіть два 
# сценарії з командного рядка системи. 
# Чи відображається новий файл у каталозі, де ви запускали свої сценарії? 
# Що, якщо ви додасте інший шлях до каталогу, переданого для відкриття?
# Примітка: методи запису файлів не додають символи нового рядка до ваших
# рядків; додайте явний "\n" у кінці рядка, якщо ви хочете повністю завершити
# рядок у файлі.
my_line="Hello file world!"
with open ("file_practice/myfile.txt", "w") as mf:
    mf.write(my_line)
    
with open ("file_practice/myfile.txt", "r") as mf:
    my_file=mf.read()
    print(my_file)



# Завдання 2
# Розширте програму Телефонна книга
# Функціональність програми Телефонна книга:
# Додайте нові записи 
# Пошук по імені 
# Пошук за прізвищем 
# Пошук за ПІБ
# Пошук за номером телефону
# Пошук за містом або штатом
# Видалити запис для даного номера телефону
# Оновити запис для вказаного номера телефону
# Можливість виходу з програми

# Першим аргументом програми має бути назва телефонної книги. Програма
# повинна завантажити дані JSON, якщо вони присутні в папці з програмою, 
# інакше виникне помилка. Після виходу користувача всі дані мають бути 
# збережені в завантаженому JSON.

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
        
