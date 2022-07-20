# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def find_diff(mynums):
    number = [round(a - int(a), 2) for a in(mynums)]
   
    number = [a for a in number if type(a) == float]
   
    return max(number) - min(number)


list = [1.1, 1.2, 3.1, 5, 10.01]
print(list, '= >', find_diff(list))