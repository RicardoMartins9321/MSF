import numpy as np
import matplotlib.pyplot as plt

dt = 0.005 # INPUT 
tf = 3 # de 0 a 3 segundos
t0 = 0
n = int((tf-t0)/dt+0.1)
print('n = ',n)

t = np.zeros(n+1)
vy = np.zeros(n+1)
y = np.zeros(n+1)

g = 9.80
v0y = 0
y0 = 0
t[0] = t0
vy[0] = v0y
y[0] = y0


for i in range(n): # Método de Euler
    t[i+1]=t[i]+dt
    ax=g
    y[i+1]=y[i]+vy[i]*dt
    vy[i+1]=vy[i]+ax*dt

for i in range(n-1):  # calcular o valor da velocidade em t=3s
    # define a margem de valores que queremos obter
    if ((t[i+1] > (2-2*dt) and t[i+1] < (2+2*dt))):
        print("dt, t, vy = ", dt, t[i+1], vy[i+1])

print("R: t=2s, y = 19.6 m")

plt.xlabel("Passo (s)")
plt.ylabel("Desvio (m)")
plt.xlim(-0.1, 0.6)
plt.ylim(-1, 6)
plt.title("Posição ao longo do tempo")
plt.plot(t, vy, color="orange")
plt.scatter(color="blue")

plt.show()

# desvio é proporcional ao passo