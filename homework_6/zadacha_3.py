# Задайте список из N элементов, заполненных числами из промежутка [-N, N].


def enter_coords():
    while True:
        try:
            coord = input("Введите позиции через пробел: ")
            coords = coord.split(" ")
            break
        except ValueError:
            print("Введите целые числа через пробел")
    return coords
    
def multiply_elements(list: list, coords: list):
    multiply = 1
    for element in coords:
        multiply *= list[int(element)]
    return multiply

n = int(input('Введите числа: ') )

# numbers = get_numbers(n)
f = lambda numbers: list(range(-n , n + 1)) # заменил этой строкой функцию создания списка от -n до n
coords = enter_coords()
print(f(n))
print(multiply_elements(f(n), coords))