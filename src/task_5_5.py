# В массиве целых чисел с количеством элементов 19 определить максимальное
# число и заменить им все четные по значению элементы. [02-4.1-BL19]
import random
random.randint

new_list = []
a = 0
while a < 19:
    new_list.append(random.randint(-100, 100))
    a += 1
print(new_list)
print(max(new_list))