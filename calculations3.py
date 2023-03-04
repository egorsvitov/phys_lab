from matplotlib import pyplot as plt
import numpy as np

def k_error(x, y, k, n):
    return np.sqrt((np.mean(y**2) - np.mean(y)**2)/(np.mean(x**2) - np.mean(x)**2) - k**2)/np.sqrt(n)

time = []
pressure = []

with open("worse2.txt", "r") as file:
    lines = file.readlines()
    P_1 = float((lines)[0].split()[1])
    for line in lines:
        [lhs, rhs] = [float(val) for val in line.split()]
        time.append(lhs)
        pressure.append(rhs)

k, b = np.polyfit(time, pressure, 1)
mnk_x = [0, max(time)]
mnk_y = [b, max(time)*k+b]

fig, pt = plt.subplots(figsize=(8, 6), dpi=400)
pt.axis(xmin=0, ymin=0, ymax=1.1*max(pressure), xmax=1.1*max(time))
pt.set_xlabel('t, с')
pt.set_ylabel('$P$')
pt.errorbar(time, pressure, fmt='o', yerr=0.1, label='Получено экспериментально')
pt.plot(mnk_x, mnk_y, label="По МНК")
pt.minorticks_on()
pt.grid(which='major')
pt.grid(which='minor', linestyle=':')
pt.legend()
fig.savefig('diagram2_3.png')

time = np.array(time)
pressure = np.array(pressure)

print(k)
print(k_error(time, pressure, k, 18))