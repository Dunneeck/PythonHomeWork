# 1.4[8]. Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# Примеры/Тесты:
# 3 2 4 -> yes
# 3 2 1 -> no

width = int(input("Введите ширину шоколадки:>> "))
long = int(input("Введите длинну шоколадки:>> "))
slice = int(input("Введите количество долек которое вы хотите отломить:>> "))

long_1, width_1 = long, width
i = 1
youCanBreakItOff = False
while i < long:
    width_1 *= i

    if slice == width_1:
        youCanBreakItOff = True
    i += 1

i = 1
while i < width:
    long_1 *= i

    if slice == long_1:
        youCanBreakItOff = True
    i += 1
print("yes" if youCanBreakItOff else "no")




