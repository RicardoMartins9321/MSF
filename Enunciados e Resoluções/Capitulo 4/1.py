import numpy as np
import matplotlib.pyplot as plt


# parámetros e condições iniciais
tf = 1.1
t0 = 0.0

x0 = 0
y0 = 0

v0 = 100/3.6
thet = 10*np.pi/180
v0x = v0*np.cos(thet)
v0y = v0*np.sin(thet)

g = 9.80
vt = 100/3.6
dres=g/vt**2

print("\nDados da trajetória de uma bola sem resistência do ar")
for dt in [0.1,0.01,0.001,0.0001,0.00001]:			# experimentar várias passos de tempo

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
    
    # método de Euler sem resistência do ar
    for i in range(n):
        t[i+1]=t[i]+dt

        ay[i] = -g
        ax[i] = 0

        vy[i+1] = vy[i] + ay[i]*dt
        vx[i+1] = vx[i] + ax[i]*dt
        
        y[i+1] = y[i] + vy[i]*dt
        x[i+1] = x[i] + vx[i]*dt

    for i in range(n):
        if dt>=0.1:
            print(f"dt {dt:.5f} \t y {max(y):.5f} m \t x {max(x):.5f} \t t {t[np.argmax(x)]:.5f}")
            break
                  
        elif y[i]*y[i+1] < 0 and dt<0.1:
            print(f"dt {dt:.5f} \t y {max(y):.5f} m \t x {x[i]:.5f} \t t {t[i]:.5f}")
            break

print(f"\nAltura máxima: {max(y):.2f} m no instante {t[np.argmax(y)]:.2f} s")
print(f"Alcance máximo: {x[i]:.2f} m no instante {t[i]:.2f} s")


print("\n\nDados da trajetória de uma bola com resistência do ar")
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
plt.plot(x, y, label="sem resistância")
plt.plot(x2, y2, label="com resistância")
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.grid()
plt.title("Trajetória de uma bola de ténis")
plt.legend()

plt.show() 
