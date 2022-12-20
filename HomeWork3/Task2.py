# Task2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

list = [10, 12, 15, 25, 16, 1, 3]
print(list)

def GetComposition(list):
    mas = []
    for i in range((len (list) + 1) // 2):
        mas.append(list [i] * list [len (list) - 1 - i])
    return mas

print(GetComposition(list))
