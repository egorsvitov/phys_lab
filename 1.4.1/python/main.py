import numpy as np
import matplotlib.pyplot as plt
from cmath import sqrt

t_1 = [31.05, 31.11, 30.91, 30.95]
t_2 = [30.48, 30.40, 30.35, 30.43]
t_3 = [30.55, 30.65, 30.49, 30.52]
t_4 = [32.07, 32.13, 32.23, 32.20]
t_5 = [31.37, 31.41, 31.33, 31.29]
t_6 = [38.45, 38.56, 38.75, 38.87]
t_7 = [31.92, 31.75, 31.63, 31.62]
a = [33.6, 29.2, 24.6, 42.9, 19.7, 9.2, 39.5]
a_s = [9.2, 19.7, 24.6, 29.2, 33.6, 39.5, 49.5]

t_8 = [31.65, 31.56, 31.61, 31.69]
t = [np.mean(t_6)/20, np.mean(t_5)/20, np.mean(t_3)/20, np.mean(t_2)/20, np.mean(t_1)/20, np.mean(t_7)/20, np.mean(t_4)/20]
u = []
v = [10**2, 20**2, 27**2, 32**2, 37**2, 43**2, 47**2]
for i in range(7):
    u.append((t[i]**2)*a_s[i])
x2 = []
y2 = []
for i in range(7):
    x2.append((v[i]/10000)**2)
    y2.append((u[i]/100)**2)


print(format(np.mean(t_1), '.3f'), '&', 0.0005, '&', format(np.std(t_1), '.3f'))
print(format(np.mean(t_2), '.3f'), '&', 0.0005, '&', format(np.std(t_2), '.3f'))
print(format(np.mean(t_3), '.3f'), '&', 0.0005, '&', format(np.std(t_3), '.3f'))
print(format(np.mean(t_4), '.3f'), '&', 0.0005, '&', format(np.std(t_4), '.3f'))
print(format(np.mean(t_5), '.3f'), '&', 0.0005, '&', format(np.std(t_5), '.3f'))
print(format(np.mean(t_6), '.3f'), '&', 0.0005, '&', format(np.std(t_6), '.3f'))
print(format(np.mean(t_7), '.3f'), '&', 0.0005, '&', format(np.std(t_7), '.3f'))
print(format(np.mean(t_8), '.3f'), '&', 0.0005, '&', format(np.std(t_8), '.3f'))

g_6_1 = ((4 * (3.1416**2) * (1**2 / 12 + (a[0]/100) ** 2) * (20 ** 2)) / ((a[0]/100) * np.mean(t_1) ** 2))
g_6_2 = ((4 * (3.1416**2) * (1**2 / 12 + (a[1]/100) ** 2) * (20 ** 2)) / ((a[1]/100) * np.mean(t_2) ** 2))
g_6_3 = ((4 * (3.1416**2) * (1**2 / 12 + (a[2]/100) ** 2) * (20 ** 2)) / ((a[2]/100) * np.mean(t_3) ** 2))
g_6_4 = ((4 * (3.1416**2) * (1**2 / 12 + (a[3]/100) ** 2) * (20 ** 2)) / ((a[3]/100) * np.mean(t_4) ** 2))
g_6_5 = ((4 * (3.1416**2) * (1**2 / 12 + (a[4]/100) ** 2) * (20 ** 2)) / ((a[4]/100) * np.mean(t_5) ** 2))
g_6_6 = ((4 * (3.1416**2) * (1**2 / 12 + (a[5]/100) ** 2) * (20 ** 2)) / ((a[5]/100) * np.mean(t_6) ** 2))
g_6_7 = ((4 * (3.1416**2) * (1**2 / 12 + (a[6]/100) ** 2) * (20 ** 2)) / ((a[6]/100) * np.mean(t_7) ** 2))

print((4 * (3.1416**2) * (1**2 / 12 + ((50-13)/100) ** 2) * (20 ** 2)) / (((50-13)/100) * np.mean(t_1) ** 2))
print((4 * (3.1416**2) * (1**2 / 12 + ((50-18)/100) ** 2) * (20 ** 2)) / (((50-18)/100) * np.mean(t_2) ** 2))
print((4 * (3.1416**2) * (1**2 / 12 + ((50-23)/100) ** 2) * (20 ** 2)) / (((50-23)/100) * np.mean(t_3) ** 2))
print((4 * (3.1416**2) * (1**2 / 12 + ((50-3)/100) ** 2) * (20 ** 2)) / (((50-3)/100) * np.mean(t_4) ** 2))
print((4 * (3.1416**2) * (1**2 / 12 + ((50-30)/100) ** 2) * (20 ** 2)) / (((50-30)/100) * np.mean(t_5) ** 2))
print((4 * (3.1416**2) * (1**2 / 12 + ((50-40)/100) ** 2) * (20 ** 2)) / (((50-40)/100) * np.mean(t_6) ** 2))
print((4 * (3.1416**2) * (1**2 / 12 + ((50-7)/100) ** 2) * (20 ** 2)) / (((50-7)/100) * np.mean(t_7) ** 2))

g_10_1 = (4 * (3.1415**2) * ((1/12) + (37/100)**2) * 400) / ((np.mean(t_1)**2) * (1 + (79.7/870.0)) * a[0]/100)
g_10_2 = (4 * (3.1415**2) * ((1/12) + (32/100)**2) * 400) / ((np.mean(t_2)**2) * (1 + (79.7/870.0)) * a[1]/100)
g_10_3 = (4 * (3.1415**2) * ((1/12) + (27/100)**2) * 400) / ((np.mean(t_3)**2) * (1 + (79.7/870.0)) * a[2]/100)
g_10_4 = (4 * (3.1415**2) * ((1/12) + (47/100)**2) * 400) / ((np.mean(t_4)**2) * (1 + (79.7/870.0)) * a[3]/100)
g_10_5 = (4 * (3.1415**2) * ((1/12) + (21/100)**2) * 400) / ((np.mean(t_5)**2) * (1 + (79.7/870.0)) * a[4]/100)
g_10_6 = (4 * (3.1415**2) * ((1/12) + (10/100)**2) * 400) / ((np.mean(t_6)**2) * (1 + (79.7/870.0)) * a[5]/100)
g_10_7 = (4 * (3.1415**2) * ((1/12) + (43/100)**2) * 400) / ((np.mean(t_7)**2) * (1 + (79.7/870.0)) * a[6]/100)

print('\n')
print(g_10_1)
print(g_10_2)
print(g_10_3)
print(g_10_4)
print(g_10_5)
print(g_10_6)
print(g_10_7)

fig, m = plt.subplots(figsize=(8, 6), dpi=400)
m.set_ylabel('a')
m.set_xlabel('T')
m.minorticks_on()
plt.plot([10, 50], [np.mean(t_2)/20, np.mean(t_2)/20], "--b", linewidth=1, label="Минимум")
m.plot(a_s, t, 'o-')
m.legend()
fig.savefig('T(a).png')


fig2, n = plt.subplots(figsize=(8, 6), dpi=400)
n.set_ylabel('$T^2 Xc$, c$^2$см')
n.set_xlabel('$a^2$, см$^2$')
n.plot(v, u, 'o')
k, b = (np.polyfit(v, u, 1))
x = np.array([50, 2200])
n.plot(x, k * x + b)
fig2.savefig('u(v).png')
print(np.polyfit(v, u, 1))
print(sqrt((np.mean(y2) - np.mean(u)**2)/(np.mean(x2)-np.mean(v)**2) - k**2)/sqrt(7))
