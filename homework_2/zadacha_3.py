# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Пример:

#- Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

def sequence_list(number: float) -> list:
    tmp_list = []

    for i in range(1, number+1):
        tmp_list.append((1 + 1 / i) ** i)

    return tmp_list

def sum_floats_in_list(list: list) -> float:
    sum = 0

    for i in list:
        sum += i

    return sum

num = int(input('\n Введите N: '))
list = sequence_list(num)
sum = sum_floats_in_list(list)
print(f'\n Последовательность для заданного N: \n{list}')
print(f'\n Сумма элементов последовательности равна {sum}\n')