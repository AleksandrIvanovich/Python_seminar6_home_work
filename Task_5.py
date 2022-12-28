# 5 - Есть список случайных чисел в промежутке от 1 до 200, количеством 200. 
# Создайте список кортежей, первый элемент которого - индекс элемента, а второй - сам элемент, при условии, что они не совпадают.
# [1,1,1,1] -> [(0,1),(1,1),(2,1),(3,1)] -> [(0,1),(2,1),(3,1)]

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
  
random_list = getting_list_random_numbers(length_lst, max_num_lst)
list_of_tuples = list(enumerate(random_list))
result_list = []
list_of_matches = []

for a in list_of_tuples: 
    if a[0] == a[1]:
        list_of_matches.append(a)
    else:    
        result_list.append(a)
        
if list_of_matches == []:
    print(f'Совпадений нет') 
    print(f'Исходный список кортежей: {list_of_tuples}')
else:  
    print(f'Совпадение индекса и числа: {list_of_matches}')
    print(f'Результирующий список кортежей: {result_list}') 
     