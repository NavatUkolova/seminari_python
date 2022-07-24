# Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.

n = 300
def simple_number(n: int):
    for dev in range (2, n):
        if n%dev == 0: 
            return False
    else:
        return True
def multiplier_of_the_number(n):
    list = []
    for i in range(2,n+1):
        if n % i == 0 and simple_number(i):
            list.append(i)
    return list

print(f' - Cписок простых множетелей числа {n}: ', multiplier_of_the_number(n))