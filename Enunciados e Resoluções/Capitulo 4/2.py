import numpy as np
import matplotlib.pyplot as plt


# parámetros e condições iniciais
tf = 2
t0 = 0.0

x0 = 0
y0 = 3

v0 = 200/3.6
thet = 10*np.pi/180
v0x = v0*np.cos(thet)
v0y = v0*np.sin(thet)

g = 9.80
vt = 6.8
dres=g/vt**2


for dt in [0.1,0.01,0.001,0.0001,0.00001]:			# experimentar várias passos de tempo

    # criar variáveis
    n2=int((tf-t0)/dt+0.1)	# +0.1 para garantir não arredondar para baixo
    t2=np.zeros(n2+1)		    # n+1 elementos; último índice n
    x2=np.zeros(n2+1)
    vx2=np.zeros(n2+1)
    y2=np.zeros(n2+1)
    vy2=np.zeros(n2+1)
    ax2=np.zeros(n2+1)
    ay2=np.zeros(n2+1)
    
    # valores iniciais
    vx2[0]=v0x
    vy2[0]=v0y
    t2[0]=t0
    x2[0]=x0
    y2[0]=y0
    
    # método de Euler com resistência do ar
    for i in range(n2):
        t2[i+1]=t2[i]+dt
        vv=np.sqrt(vx2[i]**2+vy2[i]**2)
        ax2[i]=-dres*vv*vx2[i]
        ay2[i]=-g-dres*vv*vy2[i]

        vx2[i+1]=vx2[i]+ax2[i]*dt  
        vy2[i+1]=vy2[i]+ay2[i]*dt 
                    
        x2[i+1]=x2[i]+vx2[i]*dt  
        y2[i+1]=y2[i]+vy2[i]*dt 

    for j in range(n2):
        if dt>=0.1:
            print(f"dt {dt:.5f} \t y {max(y2):.5f} m \t x {max(x2):.5f} \t t {t2[np.argmax(x2)]:.5f}")
            break
                  
        elif y2[j]*y2[j+1] < 0 and dt<0.1:
            print(f"dt {dt:.5f} \t y {max(y2):.5f} m \t x {x2[j]:.5f} \t t {t2[j]:.5f}")
            break

print(f"\nAltura máxima: {max(y2):.2f} m no instante {t2[np.argmax(y2)]:.2f} s")
print(f"Alcance máximo: {x2[j]:.2f} m no instante {t2[j]:.2f} s")


# plotar o gráfico
plt.plot(x2, y2)
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.ylim(0, 5)
plt.grid()
plt.title("Trajetória do volante de badminton")

plt.show()
