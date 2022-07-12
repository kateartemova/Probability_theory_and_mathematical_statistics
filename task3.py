import numpy as np
from math import factorial
import matplotlib.pyplot as plt
import seaborn as sns


def combinations(k, n):   # сочетания
    return factorial(n) / (factorial(k) * factorial(n - k))

# 1. Даны значения зарплат из выборки выпускников:
# 100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150.
# Посчитать (желательно без использования статистических методов наподобие std,
# var, mean) среднее арифметическое, среднее квадратичное отклонение, смещенную
# и несмещенную оценки дисперсий, первый и третий квартили, интерквартильное
# расстояние. Найти выбросы в выборке, используя для этого "усы" из boxplot.
# В этой задаче можно использовать статистические функции.


salary = np.array([100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150])

# cреднее арифметическое
salary_mean = salary.sum() / salary.size
# salary_mean = salary.mean()
print(f'result_1 cреднее арифметическое: {salary_mean}')
# cреднее квадратичное отклонение
salary_quart = (np.sum((salary - salary_mean)**2) / salary.size)**0.5
# salary_quart = salary.std()
print(f'result_1 cреднее квадратичное отклонение: {salary_quart}')
# cмещенную дисперсию
salary_sm_disp = np.sum((salary - salary_mean)**2) / salary.size
# salary_sm_disp = salary.var()
print(f'result_1 cмещенную дисперсию: {salary_sm_disp}')
# несмещенную дисперсию
salary_no_sm_disp = np.sum((salary - salary_mean)**2) / (salary.size - 1)
# salary_no_sm_disp = salary.var(ddof=1)
print(f'result_1 несмещенную дисперсию: {salary_no_sm_disp}')
# первый и третий квартили
salary_I_kv = np.percentile(salary, 25)
print(f'result_1 первый квантиль: {salary_I_kv }')
salary_III_kv = np.percentile(salary, 75)
print(f'result_1 третий квантиль: {salary_III_kv }')
# интерквартильное расстояние
salary_interkv_dist = np.percentile(salary, 75) - np.percentile(salary, 25)
print(f'result_1 интерквартильное расстояние: {salary_interkv_dist }')
# Найти выбросы в выборке, используя для этого "усы" из boxplot
df = salary
# plt.hist(df)
# plt.show()
sns.boxplot(df, orient='v')
plt.show()

# 2. В первом ящике находится 8 мячей, из которых 5 - белые. Во втором ящике - 12
# мячей, из которых 5 белых. Из первого ящика вытаскивают случайным образом два
# мяча, из второго - 4. Какова вероятность того, что 3 мяча белые?

# 2 шара из первой корзины и 1 из второго
a_1 = combinations(2, 5) / combinations(2, 8) * combinations(1, 5) * combinations(3, 7) / combinations(4, 12)

# 1 шар из первой корзины и 2 из второго
a_2 = combinations(1, 5) * combinations(1, 3) / combinations(2, 8) * combinations(2, 5) * combinations(2, 7) \
      / combinations(4, 12)

# ниодного из первой корзины и 3 из второго
a_3 = combinations(2, 3) / combinations(2, 8) * combinations(3, 5) * combinations(1, 7) / combinations(4, 12)

a = a_1 + a_2 + a_3
print(f'result_2: {a}')


# 3. В университет на факультеты A и B поступило равное количество студентов, а
# на факультет C студентов поступило столько же, сколько на A и B вместе.
# Вероятность того, что студент факультета A сдаст первую сессию, равна 0.8.
# Для студента факультета B эта вероятность равна 0.7, а для студента факультета
# C - 0.9. Студент сдал первую сессию. Какова вероятность, что он учится:
# a). на факультете A
# б). на факультете B
# в). на факультете C?

a = 1/4 * 0.8 + 1/4 * 0.7 + 1/2 * 0.9

result_3_1 = (1/4 * 0.8) / a
print(f'result_3 a: {result_3_1}')

result_3_2 = (1/4 * 0.7) / a
print(f'result_3 b: {result_3_2}')

result_3_3 = (1/2 * 0.9) / a
print(f'result_3 c: {result_3_3}')

# 4. Устройство состоит из трех деталей. Для первой детали вероятность выйти из
# строя в первый месяц равна 0.1, для второй - 0.2, для третьей - 0.25. Какова
# вероятность того, что в первый месяц выйдут из строя:
# а). все детали
# б). только две детали
# в). хотя бы одна деталь
# г). от одной до двух деталей?

result_4_1 = 0.1 * 0.2 * 0.25
print(f'result_4 a: {result_4_1}')

result_4_2 = (1 - 0.1) * 0.2 * 0.25 + 0.1 * (1 - 0.2) * 0.25 + 0.1 * 0.2 * (1 - 0.25)
print(f'result_4 b: {result_4_2}')

result_4_3 = 1 - ((1 - 0.1) * (1 - 0.2) * (1 - 0.25))
print(f'result_4 c: {result_4_3}')

result_4_4 = (1 - 0.1) * (1 - 0.2) * 0.25 + (1 - 0.1) * 0.2 * (1 - 0.25) + 0.1 * (1 - 0.2) * (1 - 0.25) + \
             ((1 - 0.1) * 0.2 * 0.25 + 0.1 * (1 - 0.2) * 0.25 + 0.1 * 0.2 * (1 - 0.25))
print(f'result_4 d: {result_4_4}')
