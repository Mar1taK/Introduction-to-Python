# Task3 Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и
# выведите на экран их сумму.

n = int(input('Введите число: ')) 

def GetSequence(n):

    return[round((1 + 1 / x)**x, 2) for x in range (1, n + 1)]   
        
print(GetSequence(n))
print(round(sum(GetSequence(n))))