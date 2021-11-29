"""Написать программу, которая с помощью цикла for решает следующую задачу.
В последовательности чисел от 1 до N нужно вывести:
а) все чётные числа;
б) все нечётные числа
в) все числа одновременно кратные 5 и 7.
г) сумму всех чисел
д) среднее арифметическое"""

N = int(input('введите N'))
N += 1


def a(N):
    # четные
    for i in range(N):
        if i % 2 == 0:
            print(i, end=' ')


def b(N):
    # нечетные
    for i in range(N):
        if i % 2 != 0:
            print(i, end=' ')


def c(N):
    # числа одновременно кратные 5 и 7
    for i in range(N):
        if i % 5 == 0 and i % 7 == 0:
            print(i, end=' ')


def g(N):
    # сумму всех чисел
    temp_list = []
    for i in range(N):
        temp_list.append(i)

    print(sum(temp_list))


def d(N):
    # среднее арифметическое
    temp_list = []
    for i in range(N):
        temp_list.append(i)

    print(sum(temp_list) // len(temp_list))


#a(N)
#b(N)
#c(N)
#g(N)
#d(N)
