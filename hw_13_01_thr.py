
# Створіть список даних (наприклад, список чисел або рядків).
# Розробіть функцію, яка обробляє ці дані (наприклад, сортування, зміна значень тощо).
# Реалізуйте багатопоточну версію функції обробки даних, яка розділить 
# обробку між кількома потоками. Використовуйте модуль threading.

# Виміряйте час виконання обробки даних у багатопоточному та однопоточному режимах.
# Порівняйте результати та зробіть висновки щодо ефективності багатопоточної обробки.

import threading
import time
import random
import timeit

my_list = [random.randint(0, 1000000) for _ in range(990000)]
executive_time = 0

def new_function():
    global executive_time
    start_time = timeit.default_timer()
    my_list_new = [n * 2 for n in my_list]
    time.sleep(1)
    end_time = timeit.default_timer()
    executive_time = end_time - start_time
    print("The end")
    return my_list_new

def main():
    threads = []
    for _ in range(3):
        thread = threading.Thread(target=new_function)
        thread.start()  
        threads.append(thread)
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
    print(f"Time with threading: {executive_time} sec")

# для даної функції багатопоточність дає 1.2 сек, а однопоточність 1.07сек


# n=new_function()
# n=new_function()
# n=new_function()
# print(f"Time without threading: {executive_time} sec")
