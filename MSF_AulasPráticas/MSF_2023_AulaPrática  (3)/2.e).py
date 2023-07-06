'''e) Se o volante for largado de uma altura de 20 m, quanto tempo demora a atingir o solo? Compare com o tempo 
que demoraria se não houvesse resistência do ar'''

import matplotlib.pyplot as plt
import numpy as np
import sympy as sym

y0 = 20     # m
g = 9.8     # m/s^2
vT = 6.8    # m/s

# Fórmula deste exercico para a poisção ao longo do tempo:
# da y = vT**2/g * np.log(np.cosh((g*tempo)/vT))
tempo_queda_comAr = (np.arccosh(np.e**(y0*g/vT**2)))*vT/g

# Fórmula de posição em função da acelaração gravitica: x(t) = 1/2 * g * t**2
tempo_queda_semAr = np.sqrt((y0*2) / g)

velocidade = vT*np.tanh(g*tempo_queda_comAr/vT)
aceleracao = g / np.cosh((g*tempo_queda_comAr)/vT) ** 2


print("Tempo de queda com resistencia do ar:", round(tempo_queda_comAr, 1), "s")
print("Tempo de queda sem resistencia do ar:", round(tempo_queda_semAr, 1), "s")
print("Velocidade:", round(velocidade, 1), "m/s")
print("Aceleração:", round(aceleracao, 3), "m/s^2")


tempo = np.linspace(0, 4, 20)
plt.subplot(1, 2, 1)
plt.plot(tempo, vT**2/g * np.log(np.cosh((g*tempo)/vT)))
plt.title("Queda com Resistencia")
plt.xlabel("Tempo (s)")
plt.ylabel("Distancia (m)")
plt.ylim(0, 20)
plt.grid()

plt.subplot(1, 2, 2)
plt.plot(tempo, 1/2 * g * tempo**2)
plt.title("Queda sem Resistencia")
plt.xlabel("Tempo (s)")
plt.ylim(0, 20)
plt.grid()

plt.show()
