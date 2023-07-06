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

Em = np.empty(n+1)

# Método Euler Cromer
for i in range(n):
    a[i] = (-k * x[i])/m 

    v[i+1] = v[i] + a[i]*dt

    x[i+1] = x[i] + v[i+1]*dt

    Ec = 0.5*m*(v[i]**2)
    Ep = 0.5*k*(x[i]**2)
    Em[i] = Ec + Ep

Em[n] = 0.5*m*(v[n]**2) + 0.5*k*(x[n]**2)


plt.plot(t, Em)
plt.xlabel("t(s)")
plt.ylabel("Em(J)")

plt.show()
