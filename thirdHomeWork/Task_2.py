# 3.2[18]: Требуется найти в списке целых чисел самый близкий по величине элемент к заданному числу X.
# Пользователь вводит это число с клавиатуры, список можно считать заданным. 
# Введенное число не обязательно содержится в списке.
# Примеры/Тесты:
# Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 0
# Output: 2
# Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 9
# Output: 10

yourNum = int(input('Ваше число: '))

myList = [10, 5, 7, 3, 3, 2, 5, 7, 3, 8]
myList.sort()
res = []

clossest = 0

chek = myList[0] - yourNum if yourNum < myList[0] else  yourNum - myList[0]

for i in range(len(myList) - 1):
    if yourNum == myList[i + 1]:
        continue
    if (myList[i + 1] - yourNum if yourNum < myList[i + 1] else  yourNum - myList[i + 1]) < chek:        
        chek = myList[i + 1] - yourNum if yourNum < myList[i + 1] else  yourNum - myList[i + 1]
        clossest = i + 1
        
res.append(myList[clossest])


myList.reverse()
clossest = 0

chek = myList[0] - yourNum if yourNum < myList[0] else  yourNum - myList[0]

for i in range(len(myList) - 1):
    if yourNum == myList[i + 1]:
        continue
    if (myList[i + 1] - yourNum if yourNum < myList[i + 1] else  yourNum - myList[i + 1]) < chek:        
        chek = myList[i + 1] - yourNum if yourNum < myList[i + 1] else  yourNum - myList[i + 1]
        clossest = i + 1

res.append(myList[clossest])

print(f'Ближайщее число {res[0]}' if res[0] == res[1] else f'Ближайщие числа {res[0]} и {res[1]}' )
