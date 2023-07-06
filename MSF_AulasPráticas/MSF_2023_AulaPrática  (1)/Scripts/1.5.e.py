import numpy as np
import matplotlib.pyplot as plt

X = np.array([2.3, 2.2, 2.0, 1.8, 1.6, 1.4, 1.2, 1.0])
L = np.array([222.0, 207.5, 194, 171.5, 153.0, 133.0, 113.0, 92.0])

x = L
y = X

npontos = x.size


xy = x * y  # multiplicação ponto a ponto dos elementos da array
x2 = x * x
y2 = y * y

sx = x.sum()
sy = y.sum()
sxy = xy.sum()
sxx = x2.sum()
syy = y2.sum()

n = npontos
rn = n*sxy-sx*sy
rd = (n*sxx-sx**2)*(n*syy-sy**2)
r2 = rn**2/rd
r = np.sqrt(r2)
m = (n*sxy-sx*sy)/(n*sxx-sx**2)
dm = abs(m)*np.sqrt((1/r**2-1)/(n-2))
bn = sxx*sy-sx*sxy
bd = n*sxx-sx**2
b = bn/bd
db = dm*np.sqrt(sxx/n)

x_g = np.arange(80, 240, 10)  # (y,x,numero de pontos)

l_g = m*x_g + b  # Equação da reta y = mx + b

X_165 = m*165 + b

print(f"X é {X_165} quando L é 165.0cm")
