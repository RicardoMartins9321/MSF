'''b) Encontre o declive, a ordenada na origem, os erros respetivos e o coeficiente de determinação. 
É uma relação linear bem aproximada? O ciclista conseguiu manter a mesma velocidade uniforme durante o percurso?'''

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

    return m, b, r_quadrado


tempo = np.arange(0, 10, 1)
distancia = np.array([0.00, 0.735, 1.363, 1.739, 2.805, 3.814, 4.458, 4.955, 5.666, 6.329])

m, b, r_quadrado = linreg_MQ(tempo, distancia)
x_grafico = tempo
y_grafico = m * x_grafico + b
linreg_MQ(tempo, distancia, mostra_prints=True)


# v = distancia a dividir pelo intervalo de tempo
v_media = distancia[-1] / 9
print("Velocidade media do ciclista:", v_media, "km/minuto")
print("Velocidade media do ciclista pelo declive da reta:", m, "km/minuto")
print("Velocidade media do ciclista:", v_media*60, "km/h")


c1=np.polyfit(tempo,distancia,1) 
print("Reta aproximada das funções:", c1)
