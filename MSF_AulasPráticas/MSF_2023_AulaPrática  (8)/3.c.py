import numpy as np
import matplotlib.pyplot as plt

vi = 100/3.6
teta = np.radians(10)
g = 9.8
t0 = 0
tf = 1
dt = 0.001
n = int((tf-t0)/dt)
t = np.linspace(t0, tf, n)
vt = 100/3.6
m = 0.057

x = np.empty(n)
y = np.empty(n)
x[0] = 0
y[0] = 0

vx = np.empty(n)
vy = np.empty(n)
vx[0] = vi * np.cos(teta)
vy[0] = vi * np.sin(teta)

ax = np.empty(n)
ay = np.empty(n)
ax[0] = 0
ay[0] = -g

v = np.empty(n)
v[0] = vi

Em = np.empty(n)


d = g/vt**2

FresX = np.zeros(n)
FresY = np.zeros(n)
Fres = np.zeros(n)
integralX = np.zeros(n)
integralY = np.zeros(n)
integral = np.zeros(n)

for i in range(n-1):
    v[i] = np.sqrt(vx[i]**2 + vy[i]**2)
    ax[i] = -d*vx[i]*abs(v[i])
    ay[i] = -d*abs(v[i])*vy[i]-g

    vy[i+1] = vy[i] + ay[i]*dt
    vx[i+1] = vx[i] + ax[i]*dt

    y[i+1] = y[i] + vy[i] * dt
    x[i+1] = x[i] + vx[i] * dt

    Em[i] = 0.5*m*v[i]**2 + m*g*y[i]

    FresX[i] = m*-d*v[i]*vx[i]
    FresY[i] = m*-d*v[i]*vy[i]
    Fres[i] = FresX[i] + FresY[i]

    integralX[i] = dt*((FresX[0]*vx[0] + FresX[i]*vx[i])
                       * 0.5 + np.sum(FresX[1:i]*vx[1:i]))
    integralY[i] = dt*((FresY[0]*vy[0] + FresY[i]*vy[i])
                       * 0.5 + np.sum(FresY[1:i]*vy[1:i]))
    integral[i] = integralX[i]+integralY[i]


v[n-1] = np.sqrt(vx[n-1]**2 + vy[n-1]**2)
Em[n-1] = 0.5*m*v[n-1]**2 + m*g*y[n-1]


tr = Em - integral

print(np.ceil(integral[round(0)]), "J")
print(round(integral[round(0.4/dt)], 3), "J")
print(round(integral[round(0.8/dt)], 3), "J")

plt.subplot(2, 1, 1)
plt.plot(t, y, color="cyan", label="Y")
plt.ylabel("Altura (m)")
plt.ylim(0, 2)
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(t, Em, color="blue", label="Ec + Ep")
plt.plot(t, integral, color="red", label="Trabalho resistência")
plt.plot(t, tr, color="orange", label="Ec + Ep - Trabalho resisténcia")
plt.ylabel("Energia (J)")
plt.xlabel("Tempo (s)")
plt.xlim(0, 1)

plt.grid()
plt.legend()

plt.show()