# Task3. Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list = [1.1, 1.2, 3.1, 5, 10.01]
print(list)

def GetDif(list):
    dif = []
    for i in range(len(list)):
        dif.append(list[i] % 1)
    return max(dif) - min(dif)

print(round(GetDif(list), 2))
