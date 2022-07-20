# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def list_to_string(input_list:list) -> str:
    text = ''

    for item in input_list:
        text += str(item)
    return text

num = int(input('Введите число: '))
binary = list()
print(f'Число {num} в двоичной системе счисления равно ',end='')

while num > 0:
    if num%2 == 0:
        binary.append(0)
        num //= 2
    else:
        binary.append(1)
        num //= 2

binary.reverse()
s_bin = list_to_string(binary)

print(s_bin)