# b) Calcular as somas das expressões acima

import matplotlib.pyplot as plt
import numpy as np

L = np.array([92.0, 113.0, 133.0, 153.0, 171.5, 194.0, 207.5, 222])
X = np.array([1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.3])

soma_x = sum(L)
soma_y = sum(X)

print("soma_x:" , soma_x)
print("soma_y:" , soma_y)