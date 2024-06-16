
# Create a list of data (for example, a list of numbers or strings).
# Develop a function that handles this data (eg sorting, changing values, etc.).
# Implement a multi-threaded version of the data processing function that will split
# processing between multiple threads. Use the threading module.

# Measure data processing execution time in multi-threaded and single-threaded modes.
# Compare results and draw conclusions about multithreading performance.

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

# for this function, multi-threading gives 1.2 seconds, and single-threading gives 1.07 seconds

n=new_function()
n=new_function()
n=new_function()
print(f"Time without threading: {executive_time} sec")
