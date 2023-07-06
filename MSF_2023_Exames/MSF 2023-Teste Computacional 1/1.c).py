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

log_a = np.log(atividade)

m, b, r_quadrado, erro_m, erro_b = linreg_MQ(t, log_a, False)

linreg_MQ(t, log_a, True)

t_meiaVida = -np.log(2)/m
dthalf = t_meiaVida*erro_m/abs(m) #erro relativo em t1/2 = erro relativo em m
print(np.log(2))
print("O tempo de meia vida será:", round(t_meiaVida, 1), "+/-", round(dthalf, 1), "horas")

