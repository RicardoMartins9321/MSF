import numpy as np
import matplotlib.pyplot as plt

def oscHarmSimp_1D(x0,v0,k,m,n,dt,alpha):
    x=np.empty(n+1)
    v=np.empty(n+1)
    a=np.empty(n+1)
    Em = np.empty(n+1)
    x[0]=x0
    v[0]=v0
    for i in range(n):
        a[i]=(-k*x[i]-3*alpha*(x[i]**2))/m
        v[i+1]=v[i]+a[i]*dt
        x[i+1]=x[i]+v[i+1]*dt
        Em[i] = 0.5*m*(v[i]**2) + 0.5*k*(x[i]**2)+alpha*(x[i]**3)
    Em[n] = 0.5*m*(v[n]**2) + 0.5*k*(x[n]**2)+alpha*(x[n]**3)
    return x,v,a,Em


x0 = 2.2
v0 = 0
k = 1
m = 1
ti = 0
tf = 20
dt = 0.001
n = int((tf-ti)/dt)
alpha = 0.05

t = np.linspace(ti, tf, n+1)

values = oscHarmSimp_1D(x0,v0,k,m,n,dt,alpha)
x = values[0]
Em = values[3]

plt.xlabel("t (s)")
plt.ylabel("x (m)")
plt.plot(t,x)
plt.grid()
plt.show()

plt.xlabel("t (s)")
plt.ylabel("Em (J)")
plt.plot(t,Em)
plt.grid()
plt.show()