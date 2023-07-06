import numpy as np
import matplotlib.pyplot as plt

X = np.array([2.3, 2.2, 2.0, 1.8, 1.6, 1.4, 1.2, 1.0])
L = np.array([222.0, 207.5, 194, 171.5, 153.0, 133.0, 113.0, 92.0])

plt.title("First MatplotLib graphic")
plt.plot(L, X, '--', color='r')     # cria uma reta que une as coordenadas introduzidas
plt.scatter(L, X, color='g')   # cria pontos nas coordenadas introduzidas
plt.xlabel('L (cm)')
plt.ylabel('Y (cm)')
plt.show()
