# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21from cmath import sqrt

import math


def get_coordinates(text): # Функция получения координат в список
    list = []
    list.append(int(input(f'Введите координаты X {text} точки: ')))
    list.append(int(input(f'Введите координаты Y {text} точки: ')))
    return list
#-----------------------------------------------------------------------------------------------------------------------------------+
print('Введите координаты точек')
first_point_coords  = get_coordinates('первой')
second_point_coords = get_coordinates('второй')

result = math.sqrt((first_point_coords[0] - second_point_coords[0])**2 + (first_point_coords[1] - second_point_coords[1])**2)

print(f'Расстояние между двумя точками равно {result}')