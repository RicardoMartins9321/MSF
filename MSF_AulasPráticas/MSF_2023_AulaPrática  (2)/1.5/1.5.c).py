# c) De seguida calcule o declive, a ordenada na origem e o coeficiente 
#    de determinação ou de correlação r^2.

import matplotlib.pyplot as plt
import numpy as np

L = np.array([92.0, 113.0, 133.0, 153.0, 171.5, 194.0, 207.5, 222])
X = np.array([1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.3])

x = L
y = X

# measures in cm 
xi = 92.0
xf = 222.0
yi = 1.0
yf = 2.3

declive = (yf-yi) / (xf-xi)
print("Declive:", declive)

# Linear regression
def linreg_MQ(x, y, mostra_somas=False):

    if  mostra_somas:
        print("soma x:", sum(x))
        print("soma y:", sum(y))
        print("soma xy:", sum(x*y))
        print("soma x^2:", sum(x**2))
        print("soma y^2:", sum(y**2))

    N = len(x)

    m = (N*sum(x*y) - sum(x)*sum(y)) / (N*sum(x**2) - sum(x)**2)

    b = (sum(x**2)*sum(y) - sum(x)*sum(x*y)) / (N*sum(x**2) - sum(x)**2)

    r_quadrado = (N*sum(x*y) - sum(x)*sum(y))**2 / ((N*sum(x**2) - sum(x)**2) * (N*sum(y**2) - sum(y)**2))

    print("m =" , m)
    print("b =" , b)
    print("r^2 =" , r_quadrado)

    return ""


print(linreg_MQ(x, y, True))
