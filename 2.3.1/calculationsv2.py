from matplotlib import pyplot as plt
import numpy as np

def k_error(x, y, k, n):
    return np.sqrt((np.mean(y**2) - np.mean(y)**2)/(np.mean(x**2) - np.mean(x)**2) - k**2)/np.sqrt(n)

time = []
pressure = []

with open("better2.txt", "r") as file:
    lines = file.readlines()
    P_1 = float((lines)[0].split()[1])
    for line in lines:
        [lhs, rhs] = [float(val) for val in line.split()]
        time.append(lhs)
        pressure.append(rhs)

log_pressure = []

for p in pressure:
    if (p - 4.3 > 0):
        log_pressure.append((np.log(p-4.3)) - np.log(P_1))

k, b = np.polyfit(time, log_pressure, 1)
mnk_x = [0, max(time)]
mnk_y = [b, max(time)*k+b]

fig, pt = plt.subplots(figsize=(8, 6), dpi=400)
# pt.axis(xmin=0, ymin=0, ymax=1.1*max(log_pressure), xmax=1.1*max(time))
pt.set_xlabel('t, с')
pt.set_ylabel('$f(P)$')
pt.errorbar(time, log_pressure, fmt='o', yerr=0.1, label='Получено экспериментально')
pt.plot(mnk_x, mnk_y, label="По МНК")
pt.minorticks_on()
pt.grid(which='major')
pt.grid(which='minor', linestyle=':')
pt.legend()
fig.savefig('diagram2_v2.png')

time = np.array(time)
log_pressure = np.array(log_pressure)

print(k)
print(k_error(time, log_pressure, k, 25))