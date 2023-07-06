import numpy as np
import matplotlib.pyplot as plt

X = np.array([2.3, 2.2, 2.0, 1.8, 1.6, 1.4, 1.2, 1.0])
L = np.array([222.0, 207.5, 194, 171.5, 153.0, 133.0, 113.0, 92.0])

x = L
y = X

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
