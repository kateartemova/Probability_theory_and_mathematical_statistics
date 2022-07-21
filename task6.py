import numpy as np
from scipy import stats

# 1. Даны значения величины заработной платы заемщиков банка (zp) и значения их поведенческого
# кредитного скоринга (ks):
# zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110],
# ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832].
# Найдите ковариацию этих двух величин с помощью элементарных действий, а затем с помощью функции
# cov из numpy. Полученные значения должны быть равны.
# Найдите коэффициент корреляции Пирсона с помощью ковариации и среднеквадратичных отклонений двух признаков,
# а затем с использованием функций из библиотек numpy и pandas.
zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])
X = zp
Y = ks
MX = X.mean()
MY = Y.mean()
# считаем ковариацию по формуле
cov_1 = ((X - MX) * (Y - MY)).mean()
print(f'result_1 ковариация по формуле: {cov_1}')
# считаем ковариацию c помощью функции cov
cov_2 = np.cov(X, Y, ddof=0)[0, 1]
print(f'result_1 ковариация c помощью функции cov: {cov_2}')
# считаем коэффициент корреляции Пирсона по формуле
cor_1 = cov_1 / (X.std() * Y.std())
print(f'result_1 коэффициент корреляции Пирсона по формуле: {cor_1}')
# считаем коэффициент корреляции Пирсона c помощью функции corrcoef
cor_2 = np.corrcoef(zp, ks)[0, 1]
print(f'result_1 коэффициент корреляции c помощью функции corrcoef: {cor_2}')

# 2. Измерены значения IQ выборки студентов, обучающихся в местных технических вузах:
# 131, 125, 115, 122, 131, 115, 107, 99, 125, 111.
# Известно, что в генеральной совокупности IQ распределен нормально.
# Найдите доверительный интервал для математического ожидания с надежностью 0.95.
iq = np.array([131, 125, 115, 122, 131, 115, 107, 99, 125, 111])
n = iq.shape[0]
m = iq.mean()
t = stats.t.ppf(1 - 0.05 / 2, n - 1)
s = iq.std(ddof=1)
result_2 = (m - t * s / np.sqrt(n), m + t * s / np.sqrt(n))
print(f'result_2 доверительный интервал: {result_2}')

# 3. Известно, что рост футболистов в сборной распределен нормально
# с дисперсией генеральной совокупности, равной 25 кв.см. Объем выборки равен 27,
# среднее выборочное составляет 174.2. Найдите доверительный интервал для математического
# ожидания с надежностью 0.95.
d = 25
n = 27
m = 174.2
# используем правилом двух сигм
s = np.math.sqrt(d/n)
result_3 = ((m - 2 * s), (m + 2 * s))
print(f'result_3 доверительный интервал: {result_3}')