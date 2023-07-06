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
ti = 0
tf = 2000
dt = 0.0001

r0 = [0,0]
ang = np.radians(5)
vx0 = vi*np.cos(ang)
vy0 = vi*np.sin(ang)
v0 = [vx0,vy0]
vT = 12.06

dt = 0.001
n = int((tf-ti)/dt)

t = np.linspace(ti,tf,n+1)

def f(px,py,vx,vy):
    f = m*px*vx + m*py*vy
    return f

def aproxTrap(f,n,dx):
    return dx*(0.5*(f[0]+f[n])+np.sum(f[1:n]))

def resAr_2D(r0,v0,n,dt,vt):
    x=np.empty(n+1)
    y=np.empty(n+1)
    vx=np.empty(n+1)
    vy=np.empty(n+1)
    ax=np.empty(n+1)
    ay=np.empty(n+1)
    aresx = np.empty(n+1)
    aresy = np.empty(n+1)
    fun = np.empty(n)
    int_trab_res = np.empty(n)
    
    g=9.80
    x[0]=r0[0]
    y[0]=r0[1]
    vx[0]=v0[0]
    vy[0]=v0[1]
    ax[0]=0
    ay[0]=-g
    dres=g/vt**2
    
    for i in range(n):
        vv=np.sqrt(vx[i]**2 +vy[i]**2)

        aresx[i] = -P*vv*vx[i]
        ax[i]= aresx[i]
        aresy[i] = -P*vv*vy[i]
        ay[i]=-g+aresy[i]
        
        vx[i+1]=vx[i]+ax[i]*dt
        vy[i+1]=vy[i]+ay[i]*dt
        
        x[i+1]=x[i]+vx[i]*dt
        y[i+1]=y[i]+vy[i]*dt

        fun[i] = m*aresx[i]*vx[i] + m*aresy[i]*vy[i]
        int_trab_res[i] = dt*((fun[0] + fun[i])/2 + np.sum(fun[1:i]))

    return (x,y),(vx,vy),(ax,ay),int_trab_res

values = resAr_2D(r0,v0,n,dt, vT)
x = values[0][0]
y = values[0][1]
trabalho = values[3]

for i in range(n):
    if y[i]*y[i+1]<0:
        tsolo = i
        break

print(f"Trabalho: {trabalho[tsolo]:.2f} J")