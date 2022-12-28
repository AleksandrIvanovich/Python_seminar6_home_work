# 3-Сформировать список из N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

def give_int(input_string):
    while True:
        try:
            num = int(input(input_string))
            return num
        except:
            print('Попробуйте еще раз. Вы ввели не число')
          
n = give_int("Введите число (количество элементов в списке):\n") 
result_list = []
j=0

for i in range(1, n+1):   
    if i == 1:
        result_list.append(i)
    else: 
        result_list.append(result_list[j-1]*(-3))
  
print(result_list)
