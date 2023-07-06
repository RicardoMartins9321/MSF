import numpy as np
import matplotlib.pyplot as plt


m = 1
k = 1
w = np.sqrt(k/m)
t0 = 0
tf = 20
dt = 0.01
n = int((tf-t0)/dt)
xeq = 1.5
Em = 0.75

t = np.linspace(t0, tf, n)

a = np.empty(n)

x = np.empty(n)
x[0] = np.sqrt(np.sqrt((2*Em)/k) + xeq**2)

v = np.empty(n)
v[0] = 0

Ep = np.empty(n)

# Método Euler Cromer
for i in range(n-1):
    a[i] = (-2*k*(x[i]**2-xeq**2)*x[i])/m

    v[i+1] = v[i] + a[i]*dt

    x[i+1] = x[i] + v[i+1]*dt

    Ep[i] = 0.5*k*(x[i]**2 - xeq**2)**2


plt.plot(x, Ep)
plt.xlabel("t(s)")
plt.ylabel("Ep(J)")

plt.show()
