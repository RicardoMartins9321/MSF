# A aceleração é a derivada da velocidade
# ax(t) = dvx / dt

import numpy as np

# dt é o passo temporal
dt=0.001 # INPUT 
tf=4.0
t0=0
n=int((tf-t0)/dt+0.1)
print('n = ',n)

t=np.zeros(n+1)
vy=np.zeros(n+1)
y=np.zeros(n+1)

g=9.80
v0y=0
y0=0
t[0]=t0
vy[0]=v0y
y[0]=y0

for i in range(n): # Método de Euler
    ax=g
    t[i+1]=t[i]+dt
    y[i+1]=y[i]+vy[i]*dt
    vy[i+1]=vy[i]+ax*dt

