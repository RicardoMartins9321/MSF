import numpy as np
import matplotlib.pyplot as plt

y0 = 2    # m
x0 = 0    # m
ang = np.radians(30)
v0 = 15
v0x = v0 * np.cos(ang)      # m/s
v0y = v0 * np.sin(ang)
g = 9.8     # m/s^2
vT = 20   # m/s

dt = 0.0001
ti = 0
tf = 1.758

n = int((tf-ti)/dt)

D = g/(vT**2)
t = np.zeros(n+1)
t[0] = ti
x = np.empty(n+1)
y = np.empty(n+1)
x[0] = x0
y[0] = y0
v = np.empty(n+1)
v[0] = v0
vy = np.empty(n+1)
vx = np.empty(n+1)
vy[0] = v0y
vx[0] = v0x
ax = np.empty(n+1)
ay = np.empty(n+1)
ax[0] = 0
ay[0] = -g

for i in range(n):
    t[i+1]=t[i]+dt
    ay[i] = -g - D*vy[i]*v[i]
    ax[i] = - D*vx[i]*v[i]
    y[i+1] = y[i] + vy[i]*dt
    x[i+1] = x[i] + vx[i]*dt
    vx[i+1] = vx[i] + ax[i]*dt
    vy[i+1] = vy[i] + ay[i]*dt
    
for n in range(n):
    if 3-2*dt< y[n] < 3+2*dt:
        print("O objeto atinge a altura de y=3 metros em")
        print("Tempo:", round(t[n], 2), "s")
        print("Ditância eixo x:", round(x[n], 2), "m")


# O Alcance é máximo quando sen(2*angulo) for o maior possivel
# sendo assim, quando o ângulo de lançamento é 45°, o valor do seno contabilizado
# é o seno de 90° (sen2.45º = sen90º = 1), e o alcance é o máximo possível.
angulo_melhor = 45 

plt.title("Gráfico altura em função da distância")
plt.xlabel("distância (m)")
plt.ylabel("altura (m)")
plt.grid()
plt.plot(x, y, color = "blue")
plt.plot(17.97, 3, "o",color = "red")

plt.show()