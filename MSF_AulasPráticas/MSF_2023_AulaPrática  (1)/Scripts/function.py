import numpy as np
import matplotlib.pyplot as plt

def linreg_MQ(x, y, mostra_somas=False):

    if  mostra_somas:
        print("sum yi", sum(y))
        print("sum xi", sum(x))
        print("sum xiyi", sum(x*y))
        print("sum xi^2", sum(x**2))
        print("sum yi^2", sum(y**2))

    N = len(x)

    m = (N*sum(x*y) - sum(x)*sum(y)) / (N*sum(x**2) - sum(x)**2)

    b = (sum(x**2)*sum(y) - sum(x)*sum(x*y)) / (N*sum(x**2) - sum(x)**2)

    r = (N*sum(x*y) - sum(x)*sum(y))**2 / ((N*sum(x**2) - sum(x)**2) * (N*sum(y**2) - sum(y)**2))

    return m, b, r

X = np.array([2.3, 2.2, 2.0, 1.8, 1.6, 1.4, 1.2, 1.0])
L = np.array([222.0, 207.5, 194, 171.5, 153.0, 133.0, 113.0, 92.0])

x = L
y = X

print(linreg_MQ(x, y, True))