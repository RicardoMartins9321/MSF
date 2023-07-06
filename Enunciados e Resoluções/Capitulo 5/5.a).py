import matplotlib.pyplot as plt
import numpy as np

v0 = 100/3.6
teta = np.radians(10)
dt = 0.0001
g = 9.8
t0 = 0
tf = 1

vt = 100/3.6

n = int((tf-t0)/dt)
t = np.linspace(t0, tf, n)

vx = np.empty(n)
vy = np.empty(n)

ax = np.empty(n)
ay = np.empty(n)

x = np.empty(n)
y = np.empty(n)

v = np.empty(n)
Em = np.empty(n)

x[0] = 0
y[0] = 0

vx[0] = v0*np.cos(teta)
vy[0] = v0*np.sin(teta)

d = g/vt**2

for i in range(n-1):
    ay[i] = -g
    ax[i] = 0

    vy[i+1] = vy[i] + ay[i]*dt
    vx[i+1] = vx[i] + ax[i]*dt

    y[i+1] = y[i] + vy[i] * dt
    x[i+1] = x[i] + vx[i] * dt

    v[i] = np.sqrt(vx[i]**2 + vy[i]**2)
    Em[i] = 0.5*0.057*v[i]**2 + 0.057*g*y[i]

v[n-1] = np.sqrt(vx[n-1]**2 + vy[n-1]**2)
Em[n-1] = 0.5*0.057*v[n-1]**2 + 0.057*g*y[n-1]

print("Valor máximo de Em =", round(max(Em), 3), "J")

plt.subplot(2, 1, 1)
plt.plot(t, y, label="Y")
plt.ylabel("Altura (m)")
plt.legend()
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(t, Em, color="red", label="Em = Ec+Ep")
plt.ylabel("Energia (J)")
plt.xlabel("Tempo (s)")
plt.ylim(0, 25)
plt.grid()
plt.legend()

plt.show()

