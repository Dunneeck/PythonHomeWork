# 3.1[16]: Дан список целых чисел. Требуется вычислить, сколько раз встречается некоторое число X в этом списке.
# Пользователь вводит число X с клавиатуры. Список можно считать заданным.
# Если такого числа в списке нет - вывести -1.

# Примеры/Тесты:
# Input:   [10, 5, 7, 3, 3, 0, 5, 7, 2, 8], x = 3
# Output:  2

# Input:   [10, 5, 7, 3, 3, 0, 5, 7, 2, 8], x = 20
# Output:  -1
# Напишите алгоритм подсчета самостоятельно или воспользуйтесь методами списка.

# (*) Усложнение. При выводе результата на экран воспользуйтесь тернарным оператором.

myLIst = [10, 5, 7, 3, 3, 0, 5, 7, 2, 8]

yourNum = int(input("Какое число вам надо?: "))

res = 0

for i in range(len(myLIst)):
    if myLIst[i] == yourNum:
        res +=1

print(res if res > 0 else -1)
