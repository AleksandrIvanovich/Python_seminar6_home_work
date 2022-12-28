# 4 - Дан список случайных чисел. Оставьте только те, сумма цифр которых четна

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

s = (getting_list_random_numbers(length_lst,max_num_lst,))
r = []
 
for a in s:   
   a = list(map(int, str(a)))
   sum = 0
   for i in a:
      sum = sum + i
   if sum %2 == 0:
      r.append(sum)
   # print(f'Сумма {a} = {sum}')
         
          
print(s)
print(r)
      
      
    
   
    
