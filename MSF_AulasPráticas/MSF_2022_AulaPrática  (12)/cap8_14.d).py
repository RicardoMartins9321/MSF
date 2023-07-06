import numpy as np
import matplotlib.pyplot as plt

t0 = 0
tf = 50
dt = 0.01
n = int((tf-t0)/dt)
k = 1
b = 0.05
F0 = 7.5
m = 1
w = 1

t = np.linspace(t0, tf, n)

a = np.empty(n)

v = np.empty(n)
v[0] = -4

x = np.empty(n)
x[0] = -2

for i in range(n-1):
    a[i] = (-k*x[i])/m - (b*v[i])/m + (F0*np.cos(w*t[i]))/m

    v[i+1] = v[i] + a[i]*dt

    x[i+1] = x[i] + v[i+1]*dt

maxes = []
tempos = []
for i in range(n):
    if t[i] > 200:
        if x[i-1] < x[i] > x[i+1]:
            maxes.append(x[i])
            tempos.append(t[i])

amplitude = sum(maxes)/len(maxes)
print(f"Amplitude numérica: {amplitude:.3f} m")

periodos = []
for i in range(len(tempos)-1):
    periodos.append(tempos[i+1]-tempos[i])

periodo = sum(periodos)/len(periodos)
print(f"Período numérico: {periodo:.3f} s")

plt.plot(t, x)
plt.xlabel("t(s)")
plt.ylabel("x(m)")
plt.grid()
plt.show()