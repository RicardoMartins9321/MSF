import numpy as np
import matplotlib.pyplot as plt

t0 = 0
tf= 20
dt = 0.01
n = int((tf-t0)/dt)
g = 9.8

t = np.linspace(t0, tf, n)

a = np.empty(n)

w = np.empty(n)
w[0] = 0
x = np.empty(n)
x[0] = np.radians(1)

for i in range(n-1):
    a[i] = (-g/2)*np.sin(x[i])
    w[i+1] = w[i] + a[i]*dt
    x[i+1] = x[i] +w[i+1]*dt

maxes = []
tempos = []
# encontrar o ponto máximo ao verficar qual o ponto que é superior aos pontos
# diretamente antes e depois dele. 
for i in range(n):
    if x[i-1] < x[i] > x[i+1]:
        maxes.append(x[i]) # cada vez que atinge um máximo guarda esse valor de amplitude
        tempos.append(t[i]) # cada vez que atinge um máximo guarda esse valor de tempo


amplitude_numerica = sum(maxes)/len(maxes)
amplitude_analitica = max(x)
print(f"Amplitude numérica: {amplitude_numerica:.3f} m")
print(f"Amplitude analítica: {amplitude_analitica:.3f} m \n") 

periodos = []
# calcula qual o intervalo de tempo/período entre cada máximo atingido
for i in range(len(tempos)-1):
    periodos.append(tempos[i+1]-tempos[i])

periodo_numerico = sum(periodos)/len(periodos) # calcula a média de todos os valores de período
print(f"Período numérico: {periodo_numerico:.3f} s")


plt.plot(t, x)
plt.xlabel("t(s)")
plt.ylabel("x(m)")

plt.show()