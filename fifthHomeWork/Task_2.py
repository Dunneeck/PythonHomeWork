# 5.2[28]: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Циклы использовать нельзя
# Примеры/Тесты:
# <function_name>(0,0) -> 0
# <function_name>(0,2) -> 2
# <function_name>(3,0) -> 3

num1 = int(input("Введите 1 число: "))
num2 = int(input("Введите 2 число: "))

def sumNums(num1, num2, summa = 0):  
    if summa == num1 + num2:
        return summa
    return sumNums(num1, num2, summa +1)
    
    

   

print(sumNums(num1,num2))