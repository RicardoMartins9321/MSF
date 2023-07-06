import numpy as np
import matplotlib.pyplot as plt

m = 1
k = 1
b = 0.16
x0 = 2
v0 = 3

ti = 0
tf = 50
dt = 0.001
n = int((tf-ti)/dt)

t = np.linspace(ti,tf,n+1)

def oscSimpFA_1D(x0,v0,k,m,b,n,dt):
    x=np.empty(n+1)
    v=np.empty(n+1)
    a=np.empty(n+1)
    x[0]=x0
    v[0]=v0
    for i in range(n):
        a[i]=-k/m*x[i]+(-b*v[i])/m
        v[i+1]=v[i]+a[i]*dt
        x[i+1]=x[i]+v[i+1]*dt
    return x,v,a

def amp_per_comp(x, t, n):
    ind_max=[i for i in range(1,n-1) if x[i-1]<=x[i]>=x[i+1]]
    ind_min=[i for i in range(1,n-1) if x[i-1]>=x[i]<=x[i+1]]
    x_max=[x[i] for i in ind_max]
    x_min=[x[i] for i in ind_min]
    t_max=[t[i] for i in ind_max]
    x_max1=np.average(x_max)
    x_min1=np.average(x_min)

    T_lst=[t_max[i+1]-t_max[i] for i in range(len(t_max)-1)]
    T=np.average(T_lst)

    lmbd_lst=[x_max[i+1]-x_max[i] for i in range(len(x_max)-1)]
    lmbd=np.average(lmbd_lst)

    return x_max1, x_min1, T, lmbd, x_max, t_max

def regLin(x,y):
    x2=x**2
    y2=y**2
    xy=x*y
    n=x.size

    sx=x.sum()
    sy=y.sum()
    sxy=xy.sum()
    sx2=x2.sum()
    sy2=y2.sum()

    m=(n*sxy-sx*sy)/(n*sx2-(sx**2))
    b=(sx2*sy-sx*sxy)/(n*sx2-(sx**2))
    
    r2n=n*sxy-sx*sy
    r2d1=n*sx2-(sx**2)
    r2d2=n*sy2-(sy**2)
    r2=(r2n**2) / (r2d1*r2d2)
    
    varM=abs(m)*np.sqrt( ((1/r2)-1)/(n-2) )
    varB = varM*np.sqrt(sx2/n)
    return m,b,r2,varM,varB

values = oscSimpFA_1D(x0,v0,k,m,b,n,dt)
x = values[0]

values1 = amp_per_comp(x,t,n)
x_max = values1[4]
t_max = np.array(values1[5])

logX_max = np.log(x_max)

values2 = regLin(t_max,logX_max)
m = values2[0]
b = values2[1]

print("Declive:", m)
print("ordenada ma origem:", b)

plt.xlabel("t (s)")
plt.ylabel("log(x máximos)")
plt.plot(t_max,logX_max,"o")
plt.plot(t, m*t+b)
plt.grid()
plt.show()