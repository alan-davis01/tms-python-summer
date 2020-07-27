# Два натуральных числа называют дружественными, если каждое из них
# равно сумме всех делителей другого, кроме самого этого числа. Найти все
# пары дружественных чисел, лежащих в диапазоне от 200 до 300. [02-3.2-HL02]
for i in range(200,300):
    k = 0
    n = 0
    for x in range(1, int(i / 2 ) +1):
        if i % x == 0:
            k += x
    for j in range(1, int(k / 2 ) +1):
        if k % j == 0:
            n += j
    if i == n and i != k and i == min(i, k):
        print(i, k)