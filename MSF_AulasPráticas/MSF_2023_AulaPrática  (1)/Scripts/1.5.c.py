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

print("{:13}{:13}{:13}{:13}{:13}".format("Soma do x",
      "Soma do y", "Soma do x*y", "Soma de x^2", "Soma de y^2"))
print("{:<13}{:<13}{:<13}{:<13}{:<13}".format(sx, sy, sxy, sxx, syy))

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

print()
print("m +/-dm = {:0.8f} +/- {:0.8f}".format(m, dm))
print("b +/-db = {:0.8f} +/- {:0.8f}".format(b, db))
print("r2 = {:0.8f}".format(r2))
