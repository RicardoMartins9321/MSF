
import matplotlib.pyplot as plt
import numpy as np


v0 = 10
y0 = 0
g = 9.8

t = np.arange(0, 3, 0.01)
yt = v0*t - (1/2 * g * t**2)
y_maximo = max(yt)
t_maximo = max(abs(-np.sqrt(((y_maximo-v0*t) * 2 ) / g)))


print("Valor máximo de y:", round(y_maximo, 2) , "m atingido aos", round(t_maximo, 2), "s")

plt.figure("Gráfico do movimento")
plt.title("Gráfico do movimento")
plt.xlabel("Tempo (s)")
plt.ylabel("Distancia (m)")
plt.grid()
plt.ylim(-1, 6)
plt.plot(t, yt, color="blue")

plt.show()