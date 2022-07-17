# Реализуйте алгоритм перемешивания списка.

import random

def fill_list(number: int) -> list:
    list = []
    for item in range(number):
        list.append(random.randint(-number,number))
    return list

def mix_list(list: list) -> list:
    
    for i in range(0,len(list)*3):
        first_index  = random.randint(0,len(list)-1)
        second_index = random.randint(0,len(list)-1)

        list[first_index], list[second_index] = list[second_index], list[first_index]

    return list


num = int(input('Введите размер списка: '))
print()
list = fill_list(number=num)

print(f'Сгенерированный список имеет вид {list}. ')
print(f'Перемешанный список имеет вид {mix_list(list=list)}. ')