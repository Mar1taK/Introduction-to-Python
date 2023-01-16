# Task3. Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def Power(num_A, num_B):
    if (num_B == 1):
        return (num_A)
    if (num_B != 1):
        return (num_A * Power (num_A, num_B - 1))

num_A = int(input("Введите число: "))
num_B = int(input("Введите степень: "))

print("Результат возведения в степень: ", Power(num_A, num_B))










