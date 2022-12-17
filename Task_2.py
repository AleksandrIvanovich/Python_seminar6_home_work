# 2. Найти произведение пар чисел в списке. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import random
from typing import List

def give_int(input_string):
    while True:
        try:
            num = int(input(input_string))
            return num
        except:
            print('Попробуйте еще раз. Вы ввели не число')
          
def getting_list_random_numbers(arg1: int, arg2: int) -> list: 
    user_list = [] 
    for i in range(arg1):
        user_list.append(random.randint(1,arg2))        
    return user_list  
  
length_lst = give_int("Введите число (количество элементов в списке):\n") 
max_num_lst = give_int("Введите число (максимальный элемента спискa):\n")   
 
user_list = getting_list_random_numbers(length_lst,max_num_lst)
l = len(user_list)
result_list = [user_list[i] * user_list[-1-i] for i in range(l//2 + l % 2)]

print(user_list)
print(result_list)