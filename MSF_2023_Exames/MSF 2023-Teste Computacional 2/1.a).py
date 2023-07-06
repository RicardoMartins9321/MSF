import numpy as np
import matplotlib.pyplot as plt


# parámetros e condições iniciais
tf = 1
t0 = 0.0

x0 = 0
y0 = 3
z0 = 0

v0x = 30
v0y = 0
v0z = 0
g = 9.80
vt = 20
dres=g/vt**2

w = 0
m = 0.057
ro_ar = 1.225
raio = 0.034
area = np.pi*raio**2
f_magnus = 0.5 * area * ro_ar * raio


for dt in [0.1,0.01,0.001,0.0001,0.00001]:			# experimentar várias passos de tempo

    # criar variáveis
    n2=int((tf-t0)/dt+0.1)	# +0.1 para garantir não arredondar para baixo
    t2=np.zeros(n2+1)		    # n+1 elementos; último índice n

    x2=np.zeros(n2+1)
    y2=np.zeros(n2+1)
    z2=np.zeros(n2+1)

    vx2=np.zeros(n2+1)
    vy2=np.zeros(n2+1)
    vz2=np.zeros(n2+1)

    ax2=np.zeros(n2+1)
    ay2=np.zeros(n2+1)
    az2=np.zeros(n2+1)
    
    # valores iniciais
    t2[0]=t0
    x2[0]=x0
    y2[0]=y0
    z2[0]=z0
    vx2[0]=v0x
    vy2[0]=v0y
    vz2[0]=v0z
    
    # método de Euler com resistência do ar e força de Magnus
    for i in range(n2):
        t2[i+1] = t2[i]+dt
        vv = np.sqrt(vx2[i]**2 + vy2[i]**2 + vz2[i]**2)

        ax2[i] = -dres*vv*vx2[i]
        ay2[i] = -g-dres*vv*vy2[i] 
        az2[i] = 0

        vx2[i+1] = vx2[i]+ax2[i]*dt  
        vy2[i+1] = vy2[i]+ay2[i]*dt
        vz2[i+1] = vz2[i]+az2[i]*dt         

        x2[i+1] = x2[i]+vx2[i]*dt  
        y2[i+1] = y2[i]+vy2[i]*dt
        z2[i+1] = z2[i]+vz2[i]*dt


    for j in range(n2):
        if (12 < x2[j] < 18.4) and (y2[j] > 1) and y2[j]*y2[j+1] < 0:
            print("O serviço para dt", dt, "É válido!")
            print(f"x: {x2[j]:.5f} m \ty: {y2[j]:.5f} m \tt {t2[j]:.5f} s")
            break
    else:
        print("O serviço para dt", dt, "Não é válido")

for j in range(n2):
    if y2[j]*y2[j+1] < 0:
        print(f"Alcance máximo: {x2[j]:.2f} m no instante {t2[j]:.2f} s")
        break

plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.plot(x2,y2)
plt.grid()
plt.show()