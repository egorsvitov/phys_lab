from matplotlib import pyplot as plt
import numpy as np

def k_error(x, y, k, n):
    return np.sqrt(np.mean(y**2)/np.mean(x**2) - k**2)/np.sqrt(n)

perfect_x = np.linspace(0, 130, 130)
perfect_y = [-np.log(67*np.exp(-0.177*x)+0.1)+np.log(67) for x in perfect_x]

time = []
pressure = []

with open("better.txt", "r") as file:
    lines = file.readlines()
    P_1 = float((lines)[0].split()[1])
    for line in lines:
        [lhs, rhs] = [float(val) for val in line.split()]
        time.append(lhs)
        pressure.append(rhs)

lim = np.min(pressure)
log_pressure = []
log_time = []

for t, p in enumerate(pressure):
    if (p - 4.3 > 0):
        log_pressure.append(-(np.log(p-4.3)) + np.log(P_1))
        log_time.append(t*10)

small_time = np.array([log_time[0], log_time[1], log_time[2]])
small_pressure = np.array([log_pressure[0], log_pressure[1], log_pressure[2]]) 

k, b = np.polyfit(small_time, small_pressure, 1)
mnk_x = [0, log_time[5]]
mnk_y = [0, log_time[5]*k]

fig, pt = plt.subplots(figsize=(4, 3), dpi=400)
pt.axis(xmin=0, ymin=0, ymax=1.1*max(log_pressure), xmax=1.1*max(log_time))
pt.set_xlabel('t, с')
pt.set_ylabel('$\\frac{P}{P_1}$, Торр')
pt.plot(perfect_x, perfect_y, '--', label="Построено по формуле (??) с использованием коэффициента МНК")
# pt.plot(log_time, log_pressure, 'o', ms=10, label=('Получено экспериментально'))
pt.errorbar(log_time, log_pressure, fmt='o', yerr=0.1, label='Получено экспериментально')
pt.plot(mnk_x, mnk_y, label="По МНК")
pt.minorticks_on()
pt.grid(which='major')
pt.grid(which='minor', linestyle=':')
pt.legend()
fig.savefig('diagram.png')

perfect_x2 = np.linspace(0,100,100)
perfect_y2 = [0.9*P_1*np.exp(-0.9*k*x2)+4.3 for x2 in perfect_x2]

fig2, pt2 = plt.subplots(figsize=(12, 9), dpi=400)
pt2.axis(xmin=0, ymin=0, ymax=1.1*max(log_pressure), xmax=1.1*max(log_time))
pt2.set_xlabel('t, с')
pt2.set_ylabel('$\\frac{P}{P_1}$, Торр')
pt2.errorbar(time, pressure, fmt='o', yerr=0.1, label=('Получено экспериментально'))
pt2.plot(perfect_x2, perfect_y2)
pt2.plot()
pt2.minorticks_on()
pt2.grid(which='major')
pt2.grid(which='minor', linestyle=':')
pt2.legend()
fig2.savefig('diagram2.png')

print(np.sqrt(k_error(small_time, small_pressure, k, 3)**2 + 0.002**2))