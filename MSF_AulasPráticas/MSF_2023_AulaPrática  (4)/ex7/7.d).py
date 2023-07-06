
import matplotlib.pyplot as plt
import numpy as np


v0 = 10         # m/s
vT = 100/3.6    # m/s
y0 = 0          # m
g = 9.8         # m/s^2
tf = 2.0        # s
t0 = 0          # s

dt = 0.01 
n = int((tf-t0)/dt+0.1)
print('n = ',n)

t = np.zeros(n+1)
vy = np.zeros(n+1)
ay = np.zeros(n+1)
y = np.zeros(n+1)

t[0] = t0
vy[0] = v0
y[0] = y0

dres = g/vT**2
for i in range(n): # Método de Euler
    t[i+1] = t[i]+dt
    vv = np.sqrt(vy[i]**2)
    ay[i] = -g-dres*vv*vy[i]  # formula no formulario
    vy[i+1] = vy[i]+ay[i]*dt
    y[i+1] = y[i]+vy[i]*dt


for i in range(n-1):  # calcular o valor da velocidade em t=3s
    if ((t[i+1] > (2-2*dt) and t[i+1] < (2+2*dt))):
        print("dt, t, v = ", dt, t[i+1], y[i+1])

for i in range(n-1):  # A altura é maxima quando v=0
    if vy[i] > 0-dt and vy[i+1] < 0+dt:
        print(
            f'altura máxima - tempo: {round(t[i+1], 3)}; posição: {round(y[i+1], 3)}; velocidade (m/s): {round(vy[i+1], 3)}')

    # Chega ao solo quando y=0
    if y[i] < 0+dt and y[i+1] > 0-dt and i > 3:
        print(
            f'Chegada ao solo - tempo: {round(t[i+1], 3)}; posição: {round(y[i+1], 3)}; velocidade (m/s): {round(vy[i+1], 3)}')


plt.plot(t, y)
plt.xlabel('Tempo (s)')
plt.ylabel('Posição (m)')
plt.title('Queda da bola com resistencia do ar')
plt.grid()
plt.show()