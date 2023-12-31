import matplotlib.pyplot as plt
import numpy as np

def abfourier(tp,xp,it0,it1,nf):
#
# cálculo dos coeficientes de Fourier a_nf e b_nf
#       a_nf = 2/T integral ( xp cos( nf w) ) dt   entre tp(it0) e tp(it1)
#       b_nf = 2/T integral ( xp sin( nf w) ) dt   entre tp(it0) e tp(it1)    
# integracao numerica pela aproximação trapezoidal
# input: matrizes tempo tp   (abcissas)
#                 posição xp (ordenadas) 
#       indices inicial it0
#               final   it1  (ao fim de um período)   
#       nf índice de Fourier
# output: af_bf e bf_nf  
# 
    dt=tp[1]-tp[0]
    per=tp[it1]-tp[it0]
    ome=2*np.pi/per

    s1=xp[it0]*np.cos(nf*ome*tp[it0])
    s2=xp[it1]*np.cos(nf*ome*tp[it1])
    st=xp[it0+1:it1]*np.cos(nf*ome*tp[it0+1:it1])
    soma=np.sum(st)
    
    q1=xp[it0]*np.sin(nf*ome*tp[it0])
    q2=xp[it1]*np.sin(nf*ome*tp[it1])
    qt=xp[it0+1:it1]*np.sin(nf*ome*tp[it0+1:it1])
    somq=np.sum(qt)
    
    intega=((s1+s2)/2+soma)*dt
    af=2/per*intega
    integq=((q1+q2)/2+somq)*dt
    bf=2/per*integq
    return af,bf

def maxminv(xm1,xm2,xm3,ym1,ym2,ym3):
# Máximo ou mínimo usando o polinómio de Lagrange
# Dados (input): (x0,y0), (x1,y1) e (x2,y2)
# Resultados (output): xm, ymax
    xab=xm1-xm2
    xac=xm1-xm3
    xbc=xm2-xm3
    a=ym1/(xab*xac)
    b=-ym2/(xab*xbc)
    c=ym3/(xac*xbc)
    xmla=(b+c)*xm1+(a+c)*xm2+(a+b)*xm3
    xm=0.5*xmla/(a+b+c)
    xta=xm-xm1
    xtb=xm-xm2
    xtc=xm-xm3
    ymax=a*xtb*xtc+b*xta*xtc+c*xta*xtb
    return xm, ymax

t0 = 0.0
tf = 100
dt = 0.001
n = int((tf-t0)/dt)
k = 1
m = 1
x0 = 3
v0 = 0
b = 0.05
f0 = 7.5
alpha = 0.25
wf = 1  # frequencia força externa

# a)
t = np.zeros(n+1)
x = np.zeros(n+1)
vx = np.zeros(n+1)
ax = np.zeros(n+1)
emec = np.zeros(n+1)

x[0] = x0
vx[0] = v0


for i in range(n):
    t[i+1] = t[i] + dt
    ax[i] = ((-4*alpha*x[i]**3) - b*vx[i] + f0*np.cos(wf*t[i]))/m
    vx[i+1] = vx[i] + ax[i] * dt
    x[i+1] = x[i] + vx[i+1] * dt
    emec[i] = 0.5*m*vx[i]*2 + 0.5*k*x[i]*2   # Emec = Ec + EpotElastica

plt.subplot(2,1,1)
plt.title("Posição x tempo")
plt.plot(t,x, color="blue", label="x=3.000")
plt.xlabel("t(s)")
plt.ylabel("x(m)")
plt.grid()


# c para os valores de a)
plt.subplot(2,1,2)
plt.title("velocidade x posição")
plt.plot(x,vx, color="red", label="vx para x=3.000")
plt.xlabel("x(m)")
plt.ylabel("vx(m/s)")
plt.grid()


# b)
x0 = 3.003

t = np.zeros(n+1)
x = np.zeros(n+1)
vx = np.zeros(n+1)
ax = np.zeros(n+1)
emec = np.zeros(n+1)

x[0] = x0
vx[0] = v0

for i in range(n):
    t[i+1] = t[i] + dt
    ax[i] = ((-4*alpha*x[i]**3) - b*vx[i] + f0*np.cos(wf*t[i]))/m
    vx[i+1] = vx[i] + ax[i] * dt
    x[i+1] = x[i] + vx[i+1] * dt
    emec[i] = 0.5*m*vx[i]*2 + 0.5*k*x[i]*2   # Emec = Ec + EpotElastica

plt.subplot(2,1,1)
plt.plot(t,x, color="orange", label="x=3.003")



# c para os valores de b)
plt.subplot(2,1,2)
plt.title("velocidade x posição")
plt.plot(x,vx, color="green", label="vx para x=3.003")
plt.xlabel("x(m)")
plt.ylabel("vx(m/s)")
plt.grid()


plt.legend()
plt.subplots_adjust(hspace=0.5)
plt.show()