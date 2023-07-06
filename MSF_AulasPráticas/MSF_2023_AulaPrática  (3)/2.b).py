'''b) Determine a velocidade instantânea em função do tempo, usando cálculo simbólico. Faça o gráfico da 
velocidade em função do tempo de 0 a 4 s, usando o pacote matplotlib'''

import matplotlib.pyplot as plt
import numpy as np
import sympy as sym

# depois de atribuidos estes valores já não se podem usar as variaveis para contas
t = sym.Symbol("t")
v = sym.Symbol("v")
vT = sym.Symbol("vT")
g = sym.Symbol("g")

vy = sym.Derivative((vT**2/g * sym.log(sym.cosh((g*t)/vT))), t, evaluate=True)
vy_simplificado = sym.simplify(vy)

print("Função da velocidade: ", vy_simplificado)

tempo = np.linspace(0, 4, 200)
velocidade = 6.8*np.tanh(9.8*tempo/6.8)

plt.figure("Lei do Movimento")
plt.title("Lei do Movimento")
plt.xlabel("Tempo (s)")
plt.ylabel("Velocidade (m/s)")
plt.plot(tempo, velocidade)
plt.grid()

plt.show()
