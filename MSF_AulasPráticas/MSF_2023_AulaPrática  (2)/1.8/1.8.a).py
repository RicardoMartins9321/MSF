'''Foi medida a energia por segundo (potência) emitida por um corpo negro (corpo que absorve toda a energia que incide 
nele) de área 100 cm2 em função da temperatura absoluta, T, e registada na seguinte tabela
a) Apresente estas medições num gráfico. A analisar o gráfico, 
   a relação entre a energia emitida e a temperatura é linear?'''

import matplotlib.pyplot as plt
import numpy as np

# linear regression
def linreg_MQ(x, y, mostra_prints=False):

    N = len(x)

    m = (N*sum(x*y) - sum(x)*sum(y)) / (N*sum(x**2) - sum(x)**2)

    b = (sum(x**2)*sum(y) - sum(x)*sum(x*y)) / (N*sum(x**2) - sum(x)**2)

    r_quadrado = (N*sum(x*y) - sum(x)*sum(y))**2 / ((N*sum(x**2) - sum(x)**2) * (N*sum(y**2) - sum(y)**2))

    variacao_m = abs(m) * np.sqrt((1/r_quadrado - 1) / (N-2))
    variacao_b = variacao_m * np.sqrt(sum(x*x) / N)

    if  mostra_prints:
        print("soma x:", sum(x))
        print("soma y:", sum(y))
        print("soma xy:", sum(x*y))
        print("soma x^2:", sum(x**2))
        print("soma y^2:", sum(y**2))

        print("m =" , m, "+/-", variacao_m)
        print("b =" , b, "+/-", variacao_b)
        print("r^2 =" , r_quadrado)
        print("erro m =", variacao_m)
        print("erro b =", variacao_m)

    return m, b, r_quadrado, 


temperatura = np.arange(200, 1200, 100)
energia = np.array([0.6950, 4.363, 15.53, 38.74, 75.08, 125.2, 257.9, 344.1, 557.4, 690.7])

m, b, r_quadrado = linreg_MQ(temperatura, energia)
x_grafico = temperatura
y_grafico = m * x_grafico + b
linreg_MQ(temperatura, energia, True)

plt.figure("Tempeatura/Energia")
plt.title("Tempeatura/Energia")
plt.xlabel("Temperatura (K)")
plt.ylabel("Energia (J)")
plt.scatter(temperatura, energia, color="blue")
plt.plot(x_grafico, y_grafico, color="orange")

plt.show()

print("Resposta: Não é linear")