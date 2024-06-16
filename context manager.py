# 1. Context manager for logging in:
# Create a context manager that logs the start and end times of a block of code.
# After the block completes, output the total execution time.

import time

class TimeContextManager:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        end_time = time.time()
        used_time = end_time - self.start_time
        print(f"Час початку виконання: {self.start_time}")
        print(f"Час завершення виконання: {end_time}")
        print(f"Загальний час виконання: {used_time} секунд")

with TimeContextManager():
    time.sleep(5)  



# 2. Context manager for working with files:
# Create a context manager that automatically opens and closes a file.
# When exiting the context, ensure that the changes are saved in the file.

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
