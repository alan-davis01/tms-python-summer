# Написать программу, в которой вводятся два операнда Х и Y и знак операции

# sign (+, –, /, *). Вычислить результат Z в зависимости от знака. Предусмотреть

# реакции на возможный неверный знак операции, а также на ввод Y=0 при

# делении. Организовать возможность многократных вычислений без перезагрузки

# программа (т.е. построить бесконечный цикл). В качестве символа прекращения

# вычислений принять ‘0’ (т.е. sign='0')



while True:

    sing = input(f'выберите операцию (+,-,/,*) для выхода напишите 0\n:')

    if sing == '0':

        break

    x = int(input('первое число :'))

    y = int(input('второе число :'))

    if sing == '+':

        z = x + y

        print(z)

    elif sing == '-':

        z = x - y

        print(z)

    elif sing == '/':

        z = (x / y) if y != 0 else 0

        print(z)

    elif sing == '*':

        z = x * y

        print(z)

    else:

        print('некоректный ввод :')