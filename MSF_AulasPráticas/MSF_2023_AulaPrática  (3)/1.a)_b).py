'''Um carro A segue numa estrada à velocidade constante de 70 km/h onde o limite de 
velocidade é de 40 km/h. Ao passar por um carro patrulha, este último parte em sua 
perseguição à aceleração constante de 2,0 m/s2
a) Faça o gráfico da lei do movimento do carro A e do carro patrulha, x = x(t).'''

import matplotlib.pyplot as plt
import numpy as np

v_A = 70/3.6    # m/s
aceleracao_policia = 2.0    # m/s^2

tempo = np.arange(0, 30, 0.01)     # segundos
distancia_carroA = tempo * v_A
distancia_policia = 0.5*aceleracao_policia * tempo**2

# Visto que o carro A move-se com velocidade constante o tempo de cruzamento com o outro automovel
# vai ser no momento em que  o tempo é igual a velocidade
tempo_cruzamento = v_A  # segundos
distancia_cruzamento = v_A * v_A

print("Tempo de cruzamento: ", round(tempo_cruzamento, 2), "s")
print("Distancia de cruzamento: ", round(distancia_cruzamento, 2), "m")

plt.figure("Lei do Movimento")
plt.title("Lei do Movimento")
plt.xlabel("Tempo (s)")
plt.ylabel("Distancia (m)")
plt.grid()
plt.plot(tempo, distancia_carroA, color="blue", label="Carro A")
plt.plot(tempo, distancia_policia, color="orange", label="Policia")
# plt.legend() must be positioned beneath the plot arguments in order to display the labels
plt.legend(loc="upper left")

plt.show()