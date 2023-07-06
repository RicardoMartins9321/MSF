import numpy as np
import matplotlib.pyplot as plt

dt_all = [0.25, 0.1, 0.01, 0.001, 0.0001, 0.00001]
ti = 0
tf = 1
g = 9.8
v0 = 100/3.6
ang = np.radians(10)

def Euler(dt):

    n = int((tf-ti)/dt)
    t = np.zeros(n+1)

    vx = np.empty(n+1)
    vx[0] = v0 * np.cos(ang)
    vy = np.empty(n+1)
    vy[0] = v0 * np.sin(ang)

    ax = np.empty(n+1)
    ax[0] = 0
    ay = np.empty(n+1)
    ay[0] = -g

    x = np.empty(n+1)
    x[0] = 0
    y = np.empty(n+1)
    y[0] = 0

    for i in range(n):
        t[i+1]=t[i]+dt

        ay[i] = -g
        ax[i] = 0

        vy[i+1] = vy[i] + ay[i]*dt
        vx[i+1] = vx[i] + ax[i]*dt
        
        y[i+1] = y[i] + vy[i]*dt
        x[i+1] = x[i] + vx[i]*dt

    return t, x, vx, ax, y, vy, ay, n

for dt in dt_all:
    t, x, vx, ax, y, vy, ay, n = Euler(dt)
    i = np.where(vy<0)[0][0]
    for num in range(n):
        if y[num] < 0:
            print("Alcance máximo:", round(x[num], 3), "m")
            break
    for num in range(n):
        if vy[num] <= 0:
            print("Altura máxima:", round(y[num], 3), "m")
            break
    #Cj = np.where(y*y<=0)[0][0]

    print("dt =", dt ,", Altura máxima: ", round(y[i], 3), "m")
        
        

'''for num in range(n):
    if y[num+1] * y[num] < 0:
        print("Alcance máximo:", round(x[num], 2), "m")
       ''' 

plt.plot(x, y)
plt.xlabel("X")
plt.ylabel("Y")
plt.grid()
plt.show()
