import numpy as np
import matplotlib.pyplot as plt

t0 = 0
tf= 100
dt = 0.01
n = int((tf-t0)/dt)
g = 9.8

t = np.linspace(t0, tf, n)

a = np.empty(n)

w = np.empty(n)
w[0] = 0
x = np.empty(n)
x[0] = np.radians(10)

for i in range(n-1):
    a[i] = (-g/2)*np.sin(x[i])
    w[i+1] = w[i] + a[i]*dt
    x[i+1] = x[i] +w[i+1]*dt

maxes = []
tempos = []
for i in range(n-1):
    if x[i-1] < x[i] > x[i+1]:
        maxes.append(x[i])
        tempos.append(t[i])

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