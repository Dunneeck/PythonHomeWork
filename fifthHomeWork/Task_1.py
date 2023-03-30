# 5.1[26]: Напишите рекурсивную функцию для возведения числа a в степень b.
# Разрешается использовать только операцию умножения. Циклы использовать нельзя
# Примеры/Тесты:
# <function_name>(2,0) -> 1
# <function_name>(2,1) -> 2
# <function_name>(2,3) -> 8
# <function_name>(2,4) -> 16


def degreeOfNumber(num, degree):
    if degree == 0:
        return 1
    return degreeOfNumber(num, degree - 1) * num



yourNum = int(input("Введите число: "))
degree = int(input("Введите в какую степень возвести: "))



print(f'Число {yourNum} в степени {degree} равна {degreeOfNumber(yourNum,degree)}')