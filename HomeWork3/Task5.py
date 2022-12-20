# Task5. Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.

a = int(input('Введите число: '))
print(a)
negofibonacci = [1, -1]
fibonacci = [1, 1]

for i in range(2, a):
    list = fibonacci [i - 1] + fibonacci [i - 2]
    fibonacci.append(list)
    list_nego = negofibonacci[i - 2] - negofibonacci[i - 1]
    negofibonacci.append(list_nego)

negofibonacci.reverse()
negofibonacci.append(0)

print(f'Для a = {a} => {negofibonacci+fibonacci}')