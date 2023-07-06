import numpy as np
import matplotlib.pyplot as plt

m = 1
xeq = 2
k = 1
x0 = 3
v0 = 0

ti = 0
tf = 100
dt = 0.001
n = int((tf-ti)/dt)

t = np.linspace(ti,tf,n+1)

def fourier(x0,v0,t,n,ti_estac, dt):
    x=np.empty(n+1)
    v=np.empty(n+1)
    a=np.empty(n+1)
    E=np.empty(n+1)
    
    v[0]=v0
    x[0]=x0
    cntMax=0
    ind=np.transpose([0 for i in range(1000)])
    afo=np.zeros(15)
    bfo=np.zeros(15)


    for i in range(n):
        if x[i]>0:
            a[i]=-(x[i]-xeq)
            v[i+1]=v[i]+a[i]*dt
            x[i+1]=x[i]+v[i+1]*dt
        else:
            a[i]=-x[i]-xeq
            v[i+1]=v[i]+a[i]*dt
            x[i+1]=x[i]+v[i+1]*dt
        if t[i]>ti_estac and x[i-1] < x[i] and  x[i+1] < x[i]:
            cntMax+=1
            ind[cntMax]=int(i)
    		
    t0=ind[cntMax-1]
    t1=ind[cntMax]    
    for i in range(15):
        af, bf=fourier_calc(t,x,t0,t1,dt,i)
        afo[i]=af
        bfo[i]=bf

    ii=np.linspace(0,14,15)
    plt.figure()
    plt.ylabel('| a_n |')
    plt.xlabel('n')
    plt.bar(ii,np.abs(afo))
    plt.grid()
    plt.show()



    ii=np.linspace(0,14,15)
    plt.figure()
    plt.ylabel('| b_n |')
    plt.xlabel('n')
    plt.bar(ii,np.abs(bfo))
    plt.grid()
    plt.show()
    
def fourier_calc(t,x,t0,t1,dt,nf):
    T=t[t1]-t[t0]
    ome=2*np.pi/T

    s1=x[t0]*np.cos(nf*ome*t[t0])
    s2=x[t1]*np.cos(nf*ome*t[t1])
    st=x[t0+1:t1]*np.cos(nf*ome*t[t0+1:t1])
    soma=np.sum(st)
    
    q1=x[t0]*np.sin(nf*ome*t[t0])
    q2=x[t1]*np.sin(nf*ome*t[t1])
    qt=x[t0+1:t1]*np.sin(nf*ome*t[t0+1:t1])
    somq=np.sum(qt)
    
    intega=((s1+s2)/2+soma)*dt
    af=2/T*intega
    integq=((q1+q2)/2+somq)*dt
    bf=2/T*integq
    return af,bf

fourier(x0,v0,t,n,0,dt)