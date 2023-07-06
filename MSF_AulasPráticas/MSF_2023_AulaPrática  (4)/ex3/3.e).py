import numpy as np

dt = 0.5 # INPUT 
tf = 3.0 # de 0 a 3 segundos
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
    ax=g
    t[i+1]=t[i]+dt
    y[i+1]=y[i]+vy[i]*dt
    vy[i+1]=vy[i]+ax*dt

for i in range(n-1):  # calcular o valor da velocidade em t=3s
    '''define a margem de valores que queremos obter
    # 2-2*dt e o 2+2*dt sao valores que podendo ser alterados, apenas estao definidos da
    # maneira que estão de forma a dar apenas valores perto dos 3 segundos
    # são ,por isso, um o limite inferior e o outro o limite superior '''
    if ((t[i+1] > (2-2*dt) and t[i+1] < (2+2*dt))):
        print("dt, t, v = ", dt, t[i+1], y[i+1])

print("R: t=2s, y = 14.7 m valor convergiu")