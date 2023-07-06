import numpy as np
import matplotlib.pyplot as plt

m = 1
k = 1
w = np.sqrt(k/m)
t0 = 0
tf = 20
dt = 0.01
n = int((tf-t0)/dt)

t = np.linspace(t0, tf, n+1)

a = np.empty(n+1)

x = np.empty(n+1)
x[0] = 4

v = np.empty(n+1)
v[0] = 0

# Método de Euler-Cromer
for i in range(n):
    a[i] = (-k * x[i])/m 
    v[i+1] = v[i] + a[i]*dt
    x[i+1] = x[i] + v[i+1]*dt

plt.plot(t, x)
plt.show()