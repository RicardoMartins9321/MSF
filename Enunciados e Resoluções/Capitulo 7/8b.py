import numpy as np

v0 = -3
x0 = 2
k = 1
m = 1
ti = 0
tf = 30
dt = 0.001
n = int((tf-ti)/dt)

t = np.linspace(ti,tf,n+1)

def oscHarmSimp_1D(x0,v0,k,m,n,dt):
    x=np.empty(n+1)
    v=np.empty(n+1)
    a=np.empty(n+1)
    x[0]=x0
    v[0]=v0
    for i in range(n):
        a[i]=-k/m*x[i]
        v[i+1]=v[i]+a[i]*dt
        x[i+1]=x[i]+v[i+1]*dt
    return x,v,a

def amp_per_comp(x, t, n):
    ind_max=[i for i in range(1,n-1) if x[i-1]<=x[i]>=x[i+1]]
    x_max=[x[i] for i in ind_max]
    t_max=[t[i] for i in ind_max]
    A=np.average(x_max)

    T_lst=[t_max[i+1]-t_max[i] for i in range(len(t_max)-1)]
    T=np.average(T_lst)

    lmbd_lst=[x_max[i+1]-x_max[i] for i in range(len(x_max)-1)]
    lmbd=np.average(lmbd_lst)

    return A, T, lmbd

values = oscHarmSimp_1D(x0,v0,k,m,n,dt)
x = values[0] 

values1 = amp_per_comp(x,t,n)
A = values1[0]
T = values1[1]

print("Amplitude:", A)
print("Período:", T)