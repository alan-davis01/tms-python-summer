# Задан целочисленный массив. Определить количество участков массива,
# на котором элементы монотонно возрастают (каждое следующее число
# больше предыдущего). [02-4.1-ML27]

import random
random.randint

list_1 = [random.randint(0, 20) for el in range(40)]
print(list_1)
result=0
count=0
for j in range(len(list_1)-2):
    if list_1[j+2] > list_1[j+1] > list_1[j]:
        count += 1
    elif count >= 1 and list_1[j+1] > list_1[j+2]:
        result += 1
        count = 0
if list_1[-1] > list_1[-2] > list_1[-3]:
    result += 1
print(result)
