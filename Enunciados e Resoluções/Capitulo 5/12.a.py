from turtle import color
from xml.etree.ElementPath import xpath_tokenizer
import numpy as np
import matplotlib.pyplot as plt

m = 75
C_res = 0.9     # coeficiente de resistência de ar
A = 0.3 
p_ar = 1.225    # densidade do ar
u = 0.004       # coeficiente de resistência
g = 9.8
P = 0.4 * 735.4975
vi = 1
t0 = 0
tf = 1000
dt = 0.001
tolerancia = 0.000999

n = int(tf/dt)
t = np.linspace(t0, tf, n)

ax = np.empty(n)
vx = np.empty(n)
x = np.empty(n)
v = np.empty(n)

ax[0] = 0
vx[0] = vi
x[0] = 0
v[0] = vi


for i in range(n-1):
    v[i] = np.sqrt(vx[i]**2)
    ax[i] = P/(m*v[i]) - (C_res/(2*m))*A*p_ar*vx[i]*v[i] -u*g
    vx[i+1] = vx[i] + ax[i]*dt
    x[i+1] = x[i] + vx[i]*dt

    v[n-1] = np.sqrt(vx[n-1]**2)
    
    
print("Velociadade Terminal = ", round(np.max(vx), 3), "m/s")
        

plt.plot(t, v, color="red")
plt.xlabel("Tempo (s)")
plt.ylabel("Velocidade (m/s)")
plt.grid()
#plt.show()
