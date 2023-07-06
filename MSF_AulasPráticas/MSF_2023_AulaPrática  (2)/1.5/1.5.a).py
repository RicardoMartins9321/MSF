# a)  Comece por representar os dados experimentais num gráfico. 

import matplotlib.pyplot as plt
import numpy as np

L = np.array([92.0, 113.0, 133.0, 153.0, 171.5, 194.0, 207.5, 222])
X = np.array([1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.3])

x = L
y = X

plt.figure("Linear regression graphic")
plt.title("Linear regression graphic")
plt.xlabel("Length (cm)")
plt.ylabel("Distance (cm)") 
plt.scatter(x, y)
plt.show()
