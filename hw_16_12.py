# 1. Контекстний менеджер для логування:
# Створіть контекстний менеджер, який логує час початку та завершення блоку коду.
# Після завершення блоку виведіть загальний час виконання.

# import time

# class TimeContextManager:
#     def __enter__(self):
#         self.start_time = time.time()
#         return self

#     def __exit__(self, exception_type, exception_value, traceback):
#         end_time = time.time()
#         used_time = end_time - self.start_time
#         print(f"Час початку виконання: {self.start_time}")
#         print(f"Час завершення виконання: {end_time}")
#         print(f"Загальний час виконання: {used_time} секунд")

# with TimeContextManager():
#     time.sleep(5)  



# 2. Контекстний менеджер для роботи з файлами:
# Створіть контекстний менеджер, який автоматично відкриває та закриває файл. 
# При виході з контексту забезпечте збереження змін у файлі.

class FileContextManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exception_type, exception_value, traceback):
        if self.file:
            self.file.close()
            print(f"file {self.filename} saved.")


filename = "my_file.txt"
mode = "w"

with FileContextManager(filename, mode) as file:
    file.write("my text")
