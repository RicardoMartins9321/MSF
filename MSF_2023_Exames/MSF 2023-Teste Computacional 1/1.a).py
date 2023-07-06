import numpy as np
import matplotlib.pyplot as plt

# linear regression
def linreg_MQ(x, y, mostra_prints=False):

    N = len(x)

    m = (N*sum(x*y) - sum(x)*sum(y)) / (N*sum(x**2) - sum(x)**2)

    b = (sum(x**2)*sum(y) - sum(x)*sum(x*y)) / (N*sum(x**2) - sum(x)**2)

    r_quadrado = (N*sum(x*y) - sum(x)*sum(y))**2 / ((N*sum(x**2) - sum(x)**2) * (N*sum(y**2) - sum(y)**2))

    erro_m = abs(m) * np.sqrt((1/r_quadrado - 1) / (N-2))
    erro_b = erro_m * np.sqrt(sum(x*x) / N)

    if  mostra_prints:
        print("m =" , m, "+/-", erro_m)
        print("b =" , b, "+/-", erro_b)
        print("r^2 =" , r_quadrado)

    return m, b, r_quadrado, erro_m, erro_b

t = np.array([0, 48, 96, 144, 192, 240, 288, 336, 384]) # horas
atividade = np.array([10.03, 7.06, 4.88, 3.38, 2.26, 1.66, 1.14, 0.79, 0.58])   

m, b, r_quadrado, erro_m, erro_b = linreg_MQ(t, atividade, False)
x = t
# y = mx + b
y = m*x + b

linreg_MQ(t, atividade, True)

plt.title("Gráfico atividade em função do tempo")
plt.xlabel("tempo (horas)")
plt.ylabel("Atividade (mBq)")
plt.grid()
plt.scatter(t, atividade, color="blue")
plt.plot(x, y, color = "orange")

plt.show()

# Resposta: A relação entre a atividade e tempo não é linear uma vez que 