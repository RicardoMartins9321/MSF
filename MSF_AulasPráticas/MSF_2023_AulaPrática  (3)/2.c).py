'''c) Determine a aceleração instantânea em função do tempo, usando cálculo simbólico. faça o gráfico da aceleração
em função do tempo de 0 a 4 s, usando o pacote matplotlib'''

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

ay = sym.Derivative((vT*sym.tanh(g*t/vT)), t, evaluate=True)
ay_simplificado = sym.simplify(ay)

print("Função da velocidade: ", vy_simplificado)
print("Função da aceleração: ", ay_simplificado)

tempo = np.linspace(0, 4, 200)
velocidade = 6.8*np.tanh(9.8*tempo/6.8)
aceleracao = 9.8 / np.cosh((9.8*tempo)/6.8) ** 2

plt.figure("Lei do Movimento")
plt.title("Lei do Movimento")
plt.xlabel("Tempo (s)")
plt.ylabel("Aceleração (m/s^2)")
plt.plot(tempo, aceleracao)
plt.grid()

plt.show()
