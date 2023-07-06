import numpy as np
import matplotlib.pyplot as plt

m = 1
k = 1
w = np.sqrt(k/m)
t0 = 0
tf = 20
dt = 0.01
n = int((tf-t0)/dt)

t = np.linspace(t0, tf, n+1)

a = np.empty(n+1)

x = np.empty(n+1)
x[0] = 4

v = np.empty(n+1)
v[0] = 0

# Método Euler Cromer
for i in range(n):
    a[i] = (-k * x[i])/m 
    v[i+1] = v[i] + a[i]*dt
    x[i+1] = x[i] + v[i+1]*dt

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
periodo_analitico = 2*np.pi*np.sqrt(m/k)
print(f"Período numérico: {periodo_numerico:.3f} s")
print(f"Período analítico: {periodo_analitico:.3f} s")


plt.plot(t, x)
plt.xlabel("t(s)")
plt.ylabel("x(m)")
plt.plot(tempos[i], amplitude_analitica, marker="o", color="red", 
         label="Amplitude máxima")
plt.legend(loc="upper left")
plt.show()