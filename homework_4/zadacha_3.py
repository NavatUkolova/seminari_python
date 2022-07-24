# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

list = [1, 2, 3, 3, 3, 4, 5, 5]
list2 = []

for i in list:
    count = 0
    for j in list:
        if i == j:
            count +=1
    if count == 1:
        list2.append(i)
print(list)
print(list2)