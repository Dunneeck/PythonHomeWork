# Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.


a = int(input("С какого числа начинать: "))
b = int(input("Какая разность между числами: "))
c = int(input("Сколько чисел: "))
res = []
for i in range(0,c):
    res.append(a + i * b)

print(res)

# a1, d, n = [int(el) for el in input("Введите a1, d, n ").split()]

# def create_arith_progression(start, step, lenght):
#     return [start + step * idx for idx in range(lenght)]

# print(create_arith_progression(a1, d, n))