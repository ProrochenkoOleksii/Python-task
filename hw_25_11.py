# Завдання 1
# Напишіть програму Python для визначення кількості локальних змінних,
# оголошених у функції.
# def function(*args):
#     a = 1
#     b = 2
#     c = 3
#     local_variables = locals()
#     print(local_variables)
#     print("Total local variables:", len(local_variables) - 1)
# function()



# Завдання 2
# Напишіть програму Python для доступу до функції всередині функції 
# (Поради: використовуйте функцію, яка повертає іншу функцію)

# def func_out(my_list):
#     my_list.pop(1)
#     def func_in(my_list):
#         if len(my_list)>5:
#             my_list[0]=100
#             my_list[-1]=100
#         else:
#             pass
                
#             print(my_list)
#         return my_list
#     x=func_in(my_list)
#     return x


# my_list=[18,0,2,5,3,5,7,10]
# print(func_out(my_list))


# Завдання 3
# Напишіть функцію під назвою "choose_func", яка приймає список nums 
# і 2 функції зворотного виклику. Якщо всі числа в списку додатні, 
# виконайте першу функцію зі списку та поверніть її результат. В іншому 
# випадку поверніть результат другого

def square_nums (list_num):
    list_new=list()
    k=0
    for n in list_num:
        k=n**2
        list_new.append(k)
    # print(list_new)
    return list_new
def remove_negatives (list_num):
    for n in list_num:
        if n<=0:
            list_num.remove(n)
        else:
            pass
    # print(list_num)
    return list_num

def select_func(list_num, square_nums, remove_negatives):
    for i in list_num:
        if i>0:
            square_nums (list_num)
        else:
            remove_negatives (list_num)
    print (list_num)

    
nums1 = [1, 2, 3, 4, 5]

nums2 = [1, -2, 3, -4, 5]

a=select_func(nums1,square_nums,remove_negatives)
b=select_func(nums2,square_nums,remove_negatives)

