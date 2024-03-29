# 2.3[14]: Требуется вывести все целые степени двойки (т.е. числа вида 2^k), не превосходящие числа N.
# Примеры/Тесты:
# 10 ->
# 1
# 2
# 4
# 8
# (*) Усложнение. Вывод оформить в одну строку: числа выводить через запятую. Для этого воспользоваться параметрами функции print

# Примеры/Тесты:
# 10     -> 1,2,4,8,
# 10000  -> 1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,


limit = int(input('До какого числа показывать степени двойки: '))

two = 1

for i in range(limit):
    print(two, end = ", ")
    two *= 2
    if two > limit:
        break


# #  Красивый вывод

# limit = int(input('До какого числа показывать степени двойки: '))

# two = 1
# show_two = str(two)
# for i in range(limit):
#     two *= 2
#     if two > limit:
#         show_two += f"."
#         break 
#     show_two += f", {two}"
# print(show_two)