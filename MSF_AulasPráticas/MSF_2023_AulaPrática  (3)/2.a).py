'''Um volante de badmington foi largado de uma altura considerável em que a terminal do volante vT é 6.80 m/s.
a) Faça o gráfico da lei do movimento de y = y(t).'''

import matplotlib.pyplot as plt
import numpy as np

v_terminal = 6.80    # m/s
g = 9.8     # m/s^2


tempo = np.arange(0, 4, 0.01)     # segundos
y = v_terminal**2/g * np.log(np.cosh((g*tempo)/v_terminal)) # metros


plt.figure("Lei do Movimento")
plt.title("Lei do Movimento")
plt.xlabel("Tempo (s)")
plt.ylabel("Distancia (m)")
plt.grid()
plt.plot(tempo, y, color="blue")

plt.show()