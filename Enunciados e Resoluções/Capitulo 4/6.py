""" v =-A*w*sin(wt+d)
A =-A*w**2*cos(wt+d) """

import numpy as np
import matplotlib.pyplot as plt

k = 1
m = 1
t0 = 0
tf = 5
dt = 0.01
A = 4
psi = 0

n = int((tf-t0)/dt)
t = np.linspace(t0, tf, n)

w = np.sqrt(k/m)


a = np.empty(n)
v = np.empty(n)
x = np.empty(n)
a[0] = 0
v[0] = 0
x[0] = 4

v_analitico = -w*A*np.sin(w*t+psi)


for i in range(n-1):
    a[i] = -k*x[i]/m
    v[i+1] = v[i] + a[i]*dt
    x[i+1] = x[i]+v[i]*dt

plt.plot(t, v_analitico, color='red', label='Exato')
plt.plot(t, v, color='blue', label='Euler-Cromer')
plt.legend()
plt.xlabel('t (s)')
plt.ylabel('vxt (m)')
plt.xlim(-1, 19)
plt.grid()
plt.show()
