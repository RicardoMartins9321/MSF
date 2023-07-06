import numpy as np
import matplotlib.pyplot as plt

dt_all = [0.1, 0.01, 0.001, 0.0001, 0.00001]
ti = 0
tf = 1.35
g = 9.8
v0 = 130/3.6
vt = 100/3.6
ang = np.radians(10)

def Euler_com_resistencia(dt):

    n = int((tf-ti)/dt)
    t = np.zeros(n+1)

    x = np.empty(n+1)
    x[0] = -10
    y = np.empty(n+1)
    y[0] = 1
    z = np.empty(n+1)
    z[0] = 0

    vx = np.empty(n+1)
    vx[0] = v0 * np.cos(ang)
    vy = np.empty(n+1)
    vy[0] = v0 * np.sin(ang)
    vz = np.empty(n+1)
    vz[0] = 0

    ax = np.empty(n+1)
    ax[0] = 0
    ay = np.empty(n+1)
    ay[0] = -g
    az = np.empty(n+1)
    az[0] = 0

    
    for i in range(n):
        t[i+1]=t[i]+dt
        vv=np.sqrt(vx[i]**2 +vy[i]**2)
        dres=g/vt**2 # D

        ax[i]=-dres*vv*vx[i]
        ay[i]=-g-dres*vv*vy[i]

        vx[i+1]=vx[i]+ax[i]*dt 
        vy[i+1]=vy[i]+ay[i]*dt 

        x[i+1]=x[i]+vx[i]*dt 
        y[i+1]=y[i]+vy[i]*dt

    return t, x, vx, ax, y, vy, ay, n

for dt in dt_all:
    t, x, vx, ax, y, vy, ay, n = Euler_com_resistencia(dt)
    i = np.where(vy<0)[0][0]
    
    x_solo = (2*vx[0]*vy[0])/g
            
    print("dt =", dt ,", Altura máxima: ", round(y[i], 3), "m" , ", Alcance máximo 1: ", round(max(x), 3), "m")
    for num in range(n):
        if y[num]*y[num+1]<=0:
            print("Alcance máximo 2:", round(x[num], 3), "m \n")

    vT = round(np.max(x), 3)
    print("Alcance máximo 3:", vT, "m")  

  
        

plt.plot(x, y)
plt.xlabel("X")
plt.ylabel("Y")
plt.grid()
plt.show()
