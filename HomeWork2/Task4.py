# Task4 Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях.

from random import randint
numbers = []
for i in range(10):
    numbers.append(randint (-10,10))
print(numbers)

def GetNumber(numbers):
    count =0 
    for element in numbers:
        count +=1
    return count
print('Число элементов: ', GetNumber(numbers))

x = int(input('Задайте позицию первого элемента: '))
y = int(input('Задайте позицию второго элемента: '))

for i in range(len(numbers)):
    mult = numbers[x -1]*numbers[y - 1]
print(f'Произведение элементов равно: {numbers[x -1]} * {numbers[y -1]} =', mult)