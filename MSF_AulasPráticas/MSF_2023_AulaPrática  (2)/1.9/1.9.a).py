'''Foi medida a atividade de uma amostra do isótopo radioativo 131I tem de 5 em 5 dias. Os valores medidos da atividade com 
o tempo são, em mCi: 9.676 , 6.355, 4.261, 2.729, 1.862, 1.184, 0.7680, 0.4883, 0.3461, 0.2119
a) Apresente estas medições num gráfico. A analisar o gráfico, a relação entre a atividade e o tempo é linear'''

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

    return m, b, r_quadrado, 


tempo = np.arange(0, 50, 5)     # unidade: dias
atividade = np.array([9.676 , 6.355, 4.261, 2.729, 1.862, 1.184, 0.7680, 0.4883, 0.3461, 0.2119])

log_y = np.log(atividade)

m, b, r_quadrado = linreg_MQ(tempo, atividade)
linreg_MQ(tempo, atividade, True)


plt.figure("Atividade/Tempo")
plt.title("Atividade/Tempo")
plt.xlabel("Tempo (dias)")
plt.ylabel("Atividade (mCi)")
plt.plot(tempo, atividade, 'o', color="blue")

plt.show()
