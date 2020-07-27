# Дано число. Найти сумму и произведение его цифр.
a = 256
suma = 0
proizvedenie = 1
while a > 0:
    digit = a % 10
    suma = suma + digit
    proizvedenie = proizvedenie * digit
    a = a // 10
print("Сумма:", suma)
print("Произведение:", proizvedenie)
