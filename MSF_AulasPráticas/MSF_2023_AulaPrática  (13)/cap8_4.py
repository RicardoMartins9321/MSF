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
tf = 200
dt = 0.001
n = int((tf-t0)/dt)
k = 1
m = 1
x0 = 3
v0 = 0
b = 0.05
f0 = 7.5
alpha = 0.002
wf = 1  # frequencia força externa

t = np.zeros(n+1)
x = np.zeros(n+1)
vx = np.zeros(n+1)
ax = np.zeros(n+1)
emec = np.zeros(n+1)

x[0] = x0
vx[0] = v0


# a)
for i in range(n):
    t[i+1] = t[i] + dt
    ax[i] = (-k*x[i]*(1+2*alpha*x[i]**2) - b*vx[i] + f0*np.cos(wf*t[i]))/m
    vx[i+1] = vx[i] + ax[i] * dt
    x[i+1] = x[i] + vx[i+1] * dt
    emec[i] = 0.5*m*vx[i]*2 + 0.5*k*x[i]*2   # Emec = Ec + EpotElastica

plt.title("Posição x tempo")
plt.plot(t,x)
plt.xlabel("t(s)")
plt.ylabel("x(m)")
plt.grid()
plt.show()


# b)
peaks = []
for i in range(n):
    if(x[i-1]<x[i] and x[i]>x[i+1] and t[i]>100):
        peaks.append(i)

tmax = np.zeros(len(peaks))
xmax = np.zeros(len(peaks))
c=0
for i in peaks:
    tmax[c], xmax[c] = maxminv(t[i-1], t[i], t[i+1], x[i-1], x[i], x[i+1])
    c+=1

amplitude = np.mean(xmax)
print(f"Amplitude: {amplitude:.3f} m") 
periodo = tmax[1]-tmax[0]
print(f"Período: {periodo:.3f} s")


# c)
x_temp = x[t > 100]
t_temp = t[t > 100]
# ind=np.transpose([0 for i in range(1000)

afo = np.zeros(15)
bfo = np.zeros(15)
ind = np.argwhere(np.diff(np.sign(np.diff(x_temp))) == -2)

xp = x[peaks[0]:peaks[1]]  # slices
tp = t[peaks[0]:peaks[1]]

it1 = int((tp[len(tp)-1]-tp[0])/dt)

t0 = int(ind[-2])
t1 = int(ind[-1])
for i in range(15):

    af, bf = abfourier(t_temp, x_temp, t0, t1, i)
    afo[i] = af # isto é importante
    bfo[i] = bf # isto é importante
    print('afo = ',i,af,bf,np.sqrt(af**2+bf**2))

# numpy.linspace(start, stop, num=50)
ii = np.linspace(0, 14, 15) 
plt.figure()
plt.ylabel('| a_n |')
plt.xlabel('n')
plt.bar(ii, np.abs(afo))
plt.grid()
plt.show()


ii = np.linspace(0, 14, 15)
plt.figure()
plt.ylabel('| b_n |')
plt.xlabel('n')
plt.bar(ii, np.abs(bfo))
plt.grid()
plt.show()