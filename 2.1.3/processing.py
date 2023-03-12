from matplotlib import pyplot as plt
from os import listdir
from os.path import isfile, join
import numpy as np

def k_error(x, y, k, n):
    return np.sqrt((np.mean(y**2) - np.mean(y)**2)/(np.mean(x**2) - np.mean(x)**2) - k**2)/np.sqrt(n)

n = []
v1 = []
v2 = []
v3 = []
v4 = []

with open("dat.txt", "r") as file:
    lines = file.readlines()
    [n_0, v1_0, v2_0, v3_0, v4_0] = [float(elem) for elem in lines[0].split()]
    for line in lines:
        [n_, v1_, v2_, v3_, v4_] = [float(elem) for elem in line.split()]
        n.append(n_-1)
        v1.append(v1_-v1_0)
        v2.append(v2_-v2_0)
        v3.append(v3_-v3_0)
        v4.append(v4_-v4_0)

n_n = np.array(n)
v1_n = np.array(v1)
v2_n = np.array(v2)
v3_n = np.array(v3)
v4_n = np.array(v4)

k1, b1 = np.polyfit(n, v1_n, 1)
k2, b2 = np.polyfit(n, v2_n, 1)
k3, b3 = np.polyfit(n, v3_n, 1)
k4, b4 = np.polyfit(n, v4_n, 1)

k1_rand = k_error(n_n, v1_n, k1, 5)
k2_rand = k_error(n_n, v2_n, k2, 5)
k3_rand = k_error(n_n, v3_n, k3, 5)
k4_rand = k_error(n_n, v4_n, k4, 5)

mnk_x = [0, max(n_n)]
mnk_y1 = [b1, mnk_x[1]*k1 + b1]
mnk_y2 = [b2, mnk_x[1]*k2 + b2]
mnk_y3 = [b3, mnk_x[1]*k3 + b3]
mnk_y4 = [b4, mnk_x[1]*k4 + b4]

fig, pt = plt.subplots(figsize=(12, 8), dpi=400)
# pt.axis(xmin=0, ymin=0)
pt.set_xlabel('$n$')
pt.set_ylabel('$\\nu$')
pt.errorbar(n_n, v1_n, c='green', fmt='o', yerr=0.1, label='Температура 22.4 С')
pt.plot(mnk_x, mnk_y1, c = 'green')
pt.errorbar(n_n, v2_n, c='blue', fmt='o', yerr=0.1, label='Температура 32.1 С')
pt.plot(mnk_x, mnk_y2, c = 'blue')
pt.errorbar(n_n, v3_n, c='orange', fmt='o', yerr=0.1, label='Температура 43.9 С')
pt.plot(mnk_x, mnk_y3, c = 'orange')
pt.errorbar(n_n, v4_n, c='cyan', fmt='o', yerr=0.1, label='Температура 52.0 С')
pt.plot(mnk_x, mnk_y4, c = 'cyan')
pt.minorticks_on()
pt.grid(which='major')
pt.grid(which='minor', linestyle=':')
pt.legend()
fig.savefig('all_in_one.png')

fig, pt = plt.subplots(figsize=(8, 6), dpi=400)
# pt.axis(xmin=0, ymin=0)
pt.set_xlabel('$n$')
pt.set_ylabel('$\\nu$')
pt.errorbar(n_n, v1_n, c = 'green', fmt='o', yerr=0.1, label='Температура 22.4 C')
pt.plot(mnk_x, mnk_y1, c = 'green')
pt.minorticks_on()
pt.grid(which='major')
pt.grid(which='minor', linestyle=':')
fig.savefig('first.png')

fig, pt = plt.subplots(figsize=(8, 6), dpi=400)
# pt.axis(xmin=0, ymin=0)
pt.set_xlabel('$n$')
pt.set_ylabel('$\\nu$')
pt.errorbar(n_n, v2_n, c = 'blue', fmt='o', yerr=0.1, label='Температура 32.1 С')
pt.plot(mnk_x, mnk_y2, c = 'blue')
pt.minorticks_on()
pt.grid(which='major')
pt.grid(which='minor', linestyle=':')
fig.savefig('second.png')

fig, pt = plt.subplots(figsize=(8, 6), dpi=400)
# pt.axis(xmin=0, ymin=0)
pt.set_xlabel('$n$')
pt.set_ylabel('$\\nu$')
pt.errorbar(n_n, v3_n, c='orange', fmt='o', yerr=0.1, label='Температура 43.9 С')
pt.plot(mnk_x, mnk_y3, c = 'orange')
pt.minorticks_on()
pt.grid(which='major')
pt.grid(which='minor', linestyle=':')
fig.savefig('third.png')

fig, pt = plt.subplots(figsize=(8, 6), dpi=400)
# pt.axis(xmin=0, ymin=0)
pt.set_xlabel('$n$')
pt.set_ylabel('$\\nu$')
pt.errorbar(n_n, v4_n, c='cyan', fmt='o', yerr=0.1, label='Температура 52.0 С')
pt.plot(mnk_x, mnk_y4, c = 'cyan')
pt.minorticks_on()
pt.grid(which='major')
pt.grid(which='minor', linestyle=':')
fig.savefig('fourth.png')

print(k1, k2, k3, k4)
print(k1_rand, k2_rand, k3_rand, k4_rand)