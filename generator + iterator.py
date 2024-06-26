
# 1. Generator RandomTasks:

# Write a generator that generates random tasks for the user.
# Each task should have a description and an estimated completion time.
# The generator can create, for example, a list of tasks for a week.

import random 

task1 = "text abount task1"
task2 = "text abount task2"
task3 = "text abount task3"
task4 = "text abount task4"
task5 = "text abount task5"
task6 = "text abount task6"
task7 = "text abount task7"

task_list=[task1,task2,task3,task4,task5,task6,task7]

def RandomTasks(n):
    for i in range(n):
        my_task = random.choice(task_list)
        yield f"{i+1} day. Your work: {my_task}"

a=RandomTasks(4)
for n in a:
    print(n)


# 2. An iterator for accounting for working time usage.

# Create a WorkHoursCounter class that will be an iterator for accounting
# of working time spent. The user can add the time spent
# on different tasks, and the iterator will count the total spent
# time and display performance messages.

class WorkHoursCounter():
    def __init__(self):
        self.my_time = 0
        self.all_time = 0
        self.my_dict = {}

    def add_hours(self,hours,work):
        self.all_time += hours
        self.my_time += 1
        new_dict={work:hours}
        self.my_dict.update(new_dict)
        return f"Your hours for works: {self.my_dict}"

    def __iter__(self):
        self.i=0
        return self
    
    def __next__(self):
        if self.i < len(self.my_dict):
            self.i += 1
            result = self.my_dict[self.i - 1]
            return result
        else:
            raise StopIteration
    
    def hours_counter (self):
        productivity = self.all_time/self.my_time
        return f"Total hours: {self.all_time}. Average productivity of your working: {productivity}"
        
n = WorkHoursCounter()
i1 = n.add_hours(100,"work1")
i2 = n.add_hours(20,"work2")
i3 = n.add_hours(30,"work3")
print(i3)
a = n.hours_counter()
print(a)


