# 1- Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

from typing import List

accept_str = input('Введите наборы символов через пробел:\n')
wanted_str = input('Введите искомую строку: ')

def looking_second_occurrence(arg1:str, arg2:str) -> int:
    count = 0
    for k, item in enumerate(accept_str.split()):
        if item == wanted_str:
            count += 1
        if count == 2:
            return k
    return -1

result = looking_second_occurrence(accept_str, wanted_str)
print(f'Введенная строка: {accept_str}')
print(f'Искомая строка: {wanted_str}')
print(f'Индекс ввторого вхождения строки "{wanted_str}": {result}')

