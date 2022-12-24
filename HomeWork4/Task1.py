# Task1. Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import math

number_pi = math.pi
print('π = ', number_pi)
d = 0.001
print(f'Accuracy = {d}')
count = 0
while d < 1:
    count += 1
    d = d * 10
print(round(number_pi, count))