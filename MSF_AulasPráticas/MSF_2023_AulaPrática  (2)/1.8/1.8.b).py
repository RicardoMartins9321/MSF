'''Foi medida a energia por segundo (potência) emitida por um corpo negro (corpo que absorve toda a energia que incide 
nele) de área 100 cm2 em função da temperatura absoluta, T, e registada na seguinte tabela
a) Apresente as medições num gráfico log-log. Qual a dependência entre as quantidade energia emitida e a temperatura?'''

import matplotlib.pyplot as plt
import numpy as np

temperatura = np.arange(200, 1200, 100)
# print(temperatura)
energia = np.array([0.6950, 4.363, 15.53, 38.74, 75.08, 125.2, 257.9, 344.1, 557.4, 690.7])

log_x = np.log(temperatura)
log_y = np.log(energia)


reta_adjacente = np.polyfit(log_x, log_y, 1)
# print(reta_adjacente)

'''Neste x grafico estamos apenas a criar pontos suficientes para poder dar print no grafico
esta *0.9 e *1.1 apenas para aumentar o tamnho da reta de forma proporcional e assim
poder mostrar mais do grafico e nao so uma reta pequena comprimida aos pontos exatos'''
x_grafico = np.linspace(log_x[0]*0.9, log_x[-1]*1.1, 100)

# Fórmula: log(y) = log(c) + n * log(x) , log(c) é um log(y)
y_grafico =  reta_adjacente[1] + x_grafico * reta_adjacente[0] 
# print(x_grafico)
# print(y_grafico)


plt.figure("Tempeatura/Energia")
plt.title("Tempeatura/Energia")
plt.xlabel("Log(Temperatura)")
plt.ylabel("Log(Energia)")
plt.plot(x_grafico, y_grafico, color="orange")
plt.plot(log_x, log_y, 'o', color="blue")


plt.show()
