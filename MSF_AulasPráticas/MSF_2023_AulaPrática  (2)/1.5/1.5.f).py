'''f) Afaste da reta encontrada um dos valores medidos de y. 
Compare o coeficiente de determinação com o valor anterior. Faça 
um gráfico com os novos pontos experimentais e a nova reta.'''

import matplotlib.pyplot as plt
import numpy as np

# Linear regression
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



L = np.array([92.0, 113.0, 133.0, 153.0, 171.5, 194.0, 207.5, 222])
X = np.array([1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.3])

x = L
y = X

# measures in cm 
xi = 92.0
xf = 222.0
yi = 1.0
yf = 2.3

declive = (yf-yi) / (xf-xi)
print("Declive:", declive)

m,b, r_quadrado = linreg_MQ(x, y, mostra_prints=True)

# equação de uma reta: mx + b
x_grafico = np.arange(80, 250, 10)
y_grafico = m * x_grafico + b

# valor y para x = 165
exemplo_x = 165
exemplo_y = m * exemplo_x + b
print("Para x = 165 y =", exemplo_y, "cm")


# substituição em X do valor 2.0 para 1.3
X_alterado = np.array([1.0, 1.2, 1.4, 1.6, 1.8, 1.3, 2.2, 2.3])
m,b, r_quadrado = linreg_MQ(L, X_alterado, mostra_prints=True)

y_alterado = m * x_grafico + b


# Graphic ploting
plt.figure("Linear regression graphic")
plt.title("Linear regression graphic")
plt.xlabel("Length (cm)")
plt.ylabel("Distance (cm)")
plt.scatter(x , y, color="blue")
plt.plot(x_grafico, y_grafico, color="r", label="Ajuste com os pontos originais.")

plt.scatter(x, X_alterado, color="orange")
plt.plot(x_grafico, y_alterado, color="g", label="Ajuste com os pontos modificados.")

plt.show()