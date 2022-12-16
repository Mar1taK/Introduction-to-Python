# Task5 Реализуйте алгоритм перемешивания списка.

import random

def GetMixList(firstList):
    list = firstList[:]
    lenghtList = len(list)
    for i in range(lenghtList):
        index = random.randint(0, lenghtList - 1)
        temp = list[i]
        list[i] = list[index]
        list[index] = temp
    return list

list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
mixList = GetMixList(list)
print("Первоначальный список: ")
print(list)
print("Перемешанный список: ")
print(mixList)