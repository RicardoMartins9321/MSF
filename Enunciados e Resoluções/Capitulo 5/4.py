import numpy as np
import matplotlib.pyplot as plt

t0 = 0
tf = 1
dt = 0.1

n = int((tf-t0)/dt)

f = np.zeros(n+1)	
integral = np.zeros(n+1)	
x = np.zeros(n+1)	

n=int((tf-t0)/dt+0.1)	# +0.1 para garantir não arredondar para baixo
t=np.zeros(n+1)		    # n+1 elementos; último índice n
x=np.zeros(n+1)
vx=np.zeros(n+1)
y=np.zeros(n+1)
vy=np.zeros(n+1)
ax=np.zeros(n+1)
ay=np.zeros(n+1)

for i in range(3):
    f[i] = (i**3)/4
    integral = (3*i**2)/4 * ((f[0]+f[i])*0.5 + np.sum(f[1:i]))

print(integral)
