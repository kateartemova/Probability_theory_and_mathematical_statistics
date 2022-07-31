import numpy as np

# 1. Случайная непрерывная величина A имеет равномерное распределение на промежутке (200, 800].
# Найдите ее среднее значение и дисперсию.

a = 200
b = 800
# cреднее значение
m = (a + b)/2
print(f'result_1 cреднее значение: {m}')
# дисперсия
d = ((b - a)**2) / 12
print(f'result_1 дисперсия: {d}')

# 2. О случайной непрерывной равномерно распределенной величине B известно, что ее дисперсия равна 0.2.
# Можно ли найти правую границу величины B и ее среднее значение зная, что левая граница равна 0.5?
# Если да, найдите ее.

a = 0.5
c = np.sqrt(2.4)
b = c + a
print(f'result_2 правая граница: {b}')
b_mean = (a + b)/2
print(f'result_2 среднее значение {b_mean}')

# 3. Непрерывная случайная величина X распределена нормально и задана плотностью распределения
# f(x) = (1 / (4 * sqrt(2*pi))) * (exp(-(x+2)**2) / 32).
# Найдите:
# а). M(X)
m = -2
print(f'result_3 M(X): {m}')
# б). D(X)
d = 16
print(f'result_3 D(X): {d}')

# 4. Рост взрослого населения города X имеет нормальное распределение.
# Причем, средний рост равен 174 см, а среднее квадратичное отклонение равно 8 см.
# Какова вероятность того, что случайным образом выбранный взрослый человек имеет рост:
# а). больше 182 см
# (182 - 174 / 8) = 1 - 0.3413
result_4_a = 1 - 0.3413
print(f'result_4 больше 182 см: {result_4_a}')
# б). больше 190 см
# (190 - 174 / 8) = 2 - 0.4772
result_4_b = 1 - 0.4772
print(f'result_4 больше 190 см: {result_4_b}')
# в). от 166 см до 190 см
result_4_c = 0.3413 + 0.4772
print(f'result_4 от 166 см до 190 см: {result_4_c}')
# г). от 166 см до 182 см
result_4_d = 0.3413 + 0.3413
print(f'result_4 от 166 см до 182 см: {result_4_d}')
# д). от 158 см до 190 см
result_4_e = 0.4772 + 0.4772
print(f'result_4 от 158 см до 190 см: {result_4_e}')
# е). не выше 150 см или не ниже 190 см
# (150 - 174 / 8) = 3 - 0.49865
# (190 - 174 / 8) = 2 - 0.4772
result_4_f = 0.49865 - 0.4772
print(f'result_4 не выше 150 см или не ниже 190 см: {result_4_f}')
# ё). не выше 150 см или не ниже 198 см
# (150 - 174 / 8) = 3 - 0.49865
# (198 - 174 / 8) = 3 - 0.49865
result_4_g = - 0.49865 + 0.49865
print(f'result_4 не выше 150 см или не ниже 198 см: {result_4_g}')
# ж). ниже 166 см.
# (166 - 174 / 8) = 1 - 0.3413
result_4_h = - 0.3413 + 1
print(f'result_4 ниже 166 см: {result_4_h}')

# 5. На сколько сигм (средних квадратичных отклонений) отклоняется рост человека, равный 190 см, от
# математического ожидания роста в популяции, в которой M(X) = 178 см и D(X) = 25 кв.см?

x = 190
x_mean = 178
x_disp = 25
result_5 = (x - x_mean) / np.sqrt(x_disp)
print(f'result_5 {result_5}')