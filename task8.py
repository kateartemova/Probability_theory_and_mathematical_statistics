# 1. Провести дисперсионный анализ для определения того, есть ли различия
# среднего роста среди взрослых футболистов, хоккеистов и штангистов.
# Даны значения роста в трех группах случайно выбранных спортсменов:
# Футболисты: 173, 175, 180, 178, 177, 185, 183, 182.
# Хоккеисты: 177, 179, 180, 188, 177, 172, 171, 184, 180.
# Штангисты: 172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170.
# alpha = 0.05.

import numpy as np
from scipy import stats

fb = np.array([173, 175, 180, 178, 177, 185, 183, 182])
hc = np.array([177, 179, 180, 188, 177, 172, 171, 184, 180])
sht = np.array([172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170])

n1 = fb.shape[0]
n2 = hc.shape[0]
n3 = sht.shape[0]

y1_mean = fb.mean()
print(f'fb_mean: {y1_mean}')
y2_mean = hc.mean()
print(f'hc_mean: {y2_mean}')
y3_mean = sht.mean()
print(f'sht_mean: {y3_mean}')

y = np.concatenate([fb, hc, sht], axis=0)
y_mean = y.mean()
print(f'y_mean: {y_mean}')

# найдем Sf
S2_F = n1 * (y1_mean - y_mean) ** 2 + n2 * (y2_mean - y_mean) ** 2 + n3 * (y3_mean - y_mean) ** 2
print(f'S2_F: {S2_F}')
# найдем Sres
S2_res = ((fb - y1_mean) ** 2).sum() + ((hc - y2_mean) ** 2).sum() + ((sht - y3_mean) ** 2).sum()
print(f'S2_res: {S2_res}')

# оценки дисперсий
k = 3
n = n1 + n2 + n3
k1 = k - 1
k2 = n - k
sigma2_F = S2_F / k1
print(f'sigma2_F: {sigma2_F}')
sigma2_res = S2_res / k2
print(f'sigma2_res: {sigma2_res}')

# значение статистики T
T = sigma2_F / sigma2_res
print(f'T: {T}')

# найдём критическое значение Fcrit
alpha = 0.05
F_crit = stats.f.ppf(1 - alpha, k1, k2)
print(f'F_crit: {F_crit}')

print(f'Так как T>Fcrit, делаем вывод, что отличие среднего роста среди взрослых футболистов, '
      f'хоккеистов и штангистов действительно является статистически значимым')
