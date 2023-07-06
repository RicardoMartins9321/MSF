import numpy as np
import matplotlib.pyplot as plt

def acelera(t,x,v):
    return (-4*alpha*x**3 - b*v + f0*np.cos(wf*t))/m

def rk4_1D(t,x0,v0,dt,n):
    #método de Runge-Kutta de 4ª ordem que retorna a posição e a velocidade, requer que se defina à parte a função acel para a aceleração
    x=np.empty(n+1)
    x[0]=x0
    v=np.empty(n+1)
    v[0]=v0
    for i in range(n):
        ax1=acelera(t[i],x[i],v[i])
        c1v=ax1*dt
        c1x=v[i]*dt
        
        ax2=acelera(t[i]+dt/2,x[i]+c1x/2,v[i]+c1v/2)
        c2v=ax2*dt
        c2x=(v[i]+c1v/2)*dt
        
        ax3=acelera(t[i]+dt/2,x[i]+c2x/2,v[i]+c2v/2)
        c3v=ax3*dt
        c3x=(v[i]+c2v/2)*dt
        
        ax4=acelera(t[i]+dt/2,x[i]+c2x/2,v[i]+c2v/2)
        c4v=ax4*dt
        c4x=(v[i]+c3v)*dt
        
        x[i+1]=x[i]+(c1x+2*c2x+2*c3x+c4x)/6
        v[i+1]=v[i]+(c1v+2*c2v+2*c3v+c4v)/6
    return x,v

def euler(t,x0,v0,dt,n):
    x=np.empty(n+1)
    x[0]=x0
    v=np.empty(n+1)
    v[0]=v0
    for i in range(n):
        a=acelera(t[i],x[i],v[i])
        v[i+1]=v[i]+a*dt
        x[i+1]=x[i]+v[i]*dt
    return x,v

tf = 100
t0 = 0
dt=0.001
n = int((tf-t0)/dt)
t=np.linspace(0,tf,n+1)
v0 = 0 
x0 = 2 
k = 1
m = 1
v0 = 0
b = 0.02
f0 = 7.5
alpha = 0.15
wf = 1  # frequencia força externa

x_rk=rk4_1D(t,x0,v0,dt,n)[0]
x_eu=euler(t,x0,v0,dt,n)[0]

plt.xlabel("t (s)")
plt.ylabel("x (m)")
plt.plot(t,x_eu,label="Euler")
plt.plot(t,x_rk,label="Runge-Kutta")
plt.legend()
plt.grid()
plt.plot()
plt.show()

print("Pode calcular a lei do movimento até ao instante 15 segundos\n a partir do qual se começa a notar grandes divergências entre os valores obtidos nos dois métodos.")