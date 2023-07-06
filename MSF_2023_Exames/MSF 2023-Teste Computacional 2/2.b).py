from turtle import color
from xml.etree.ElementPath import xpath_tokenizer
import numpy as np
import matplotlib.pyplot as plt

m = 2000
Cres = 0.25
A = 2
p = 1.225
u = 0.04
g = 9.8
P = 40000
vi = 1
t0 = 0
tf = 2000
dt = 0.0001
theta = np.radians(5)

for dt in [0.01,0.001]:			# experimentar várias passos de tempo

    n = int(tf/dt)
    t = np.linspace(t0, tf, n)

    ax = np.empty(n)
    vx = np.empty(n)
    x = np.empty(n)
    v = np.empty(n)

    ax[0] = 0
    vx[0] = vi
    x[0] = 0
    v[0] = vi

    for i in range(n-1):
        v[i] = np.sqrt(vx[i]**2)
        ax[i] = -g*np.sin(theta) -u*g*np.cos(theta) -u*g - (Cres/(2*m))*A*p*(vx[i])*v[i] + P/(m*v[i])
        vx[i+1] = vx[i] + ax[i]*dt
        x[i+1] = x[i] + vx[i]*dt

        v[n-1] = np.sqrt(vx[n-1]**2)

        if x[i] < 2000 + dt and x[i+1] > 2000-dt:
            print(f"dt {dt} \tx {x[i]:.3f} \ttempo {t[i]:.3f} s")
            

for i in range(n-1):
    v[i] = np.sqrt(vx[i]**2)
    ax[i] = -g*np.sin(theta) -u*g*np.cos(theta) -u*g - (Cres/(2*m))*A*p*(vx[i])*v[i] + P/(m*v[i])
    vx[i+1] = vx[i] + ax[i]*dt
    x[i+1] = x[i] + vx[i]*dt

    v[n-1] = np.sqrt(vx[n-1]**2)

    if x[i] < 2000 + dt and x[i+1] > 2000-dt:
        break

print(f"\nx converge para: {x[i]:.2f} m no instante {t[i]:.2f} s")