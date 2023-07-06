import numpy as np
import matplotlib.pyplot as plt


# parámetros e condições iniciais
tf = 10
t0 = 0.0
dt = 0.01

x0 = 1
y0 = 0

v0x = 0
v0y = 2*np.pi
g = 4*np.pi**2


# criar variáveis
n=int((tf-t0)/dt+0.1)	# +0.1 para garantir não arredondar para baixo
t=np.zeros(n+1)		    # n+1 elementos; último índice n
x=np.zeros(n+1)
vx=np.zeros(n+1)
y=np.zeros(n+1)
vy=np.zeros(n+1)
ax=np.zeros(n+1)
ay=np.zeros(n+1)

# valores iniciais
vx[0]=v0x
vy[0]=v0y
t[0]=t0
x[0]=x0
y[0]=y0

# a) método de Euler
for i in range(n):
    t[i+1]=t[i]+dt
    r=np.sqrt(x[i]**2+y[i]**2)

    ax[i]=-g/r**3*x[i]
    ay[i]=-g/r**3*y[i]

    vx[i+1]=vx[i]+ax[i]*dt 
    vy[i+1]=vy[i]+ay[i]*dt 

    x[i+1]=x[i]+vx[i]*dt 
    y[i+1]=y[i]+vy[i]*dt

plt.plot(x, y, label="Euler")


# b) método de Euler Cromer
for i in range(n):
    t[i+1]=t[i]+dt
    r=np.sqrt(x[i]**2+y[i]**2)

    ax[i]=-g/r**3*x[i]
    ay[i]=-g/r**3*y[i]

    vx[i+1]=vx[i]+ax[i]*dt 
    vy[i+1]=vy[i]+ay[i]*dt 
    
    x[i+1]=x[i]+vx[i+1]*dt 
    y[i+1]=y[i]+vy[i+1]*dt 

plt.plot(x, y, label="Euler-Cromer")
plt.grid()
plt.title("Trajetória da Terra à volta do Sol")
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.legend()

plt.show()