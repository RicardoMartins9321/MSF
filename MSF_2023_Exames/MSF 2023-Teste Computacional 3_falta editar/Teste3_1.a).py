import numpy as np
from matplotlib import pyplot as plt

m = 1
k = 1
alpha = 0.05
x = np.arange(-8, 4, 0.01)
Ep = 0.5*k*(x**2)+alpha*(x**3)

plt.xlabel("x (m)")
plt.ylabel("Ep (J)")
plt.plot(x,Ep)
plt.grid()
plt.show()


print("Quando a energia é menor do que 7J o movimento é acelerado")
print("Se a energia total for maior do que 8J o movimento é cada vez mais acelerado.")