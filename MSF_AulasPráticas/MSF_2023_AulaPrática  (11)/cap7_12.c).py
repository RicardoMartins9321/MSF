import numpy as np
import matplotlib.pyplot as plt

m = 1
k = 1
w = np.sqrt(k/m)
t0 = 0
tf = 20
dt = 0.01
n = int((tf-t0)/dt)
xeq = 1.5
Em = 3

t = np.linspace(t0, tf, n+1)

a = np.empty(n+1)

x = np.empty(n+1)
x[0] = np.sqrt(np.sqrt((2*Em)/k) + xeq**2)

v = np.empty(n+1)
v[0] = 0

# Método Euler Cromer
for i in range(n):
    a[i] = (-2*k*(x[i]**2-xeq**2)*x[i])/m

    v[i+1] = v[i] + a[i]*dt

    x[i+1] = x[i] + v[i+1]*dt


maxes = []
tempos = []
# encontrar o ponto máximo ao verficar qual o ponto que é superior aos pontos
# diretamente antes e depois dele. 
for i in range(n):
    if x[i-1] < x[i] > x[i+1]:
        maxes.append(x[i])  # cada vez que atinge um máximo guarda esse valor de amplitude
        tempos.append(t[i]) # cada vez que atinge um máximo guarda esse valor de tempo

amplitude_numerica = sum(maxes)/len(maxes)
amplitude_analitica = max(x)
print(f"Amplitude numérica: {amplitude_numerica:.3f} m")
print(f"Amplitude analítica: {amplitude_analitica:.3f} m \n")

periodos = []
# calcula qual o intervalo de tempo/período entre cada máximo atingido
for i in range(len(tempos)-1):
    periodos.append(tempos[i+1]-tempos[i])

frequencia_numérica = 1/(sum(periodos)/len(periodos))  # calcula a média de todos os valores de período
frequencia_analitica = 1/(2*np.pi) * np.sqrt(k/m)
print(f"Frequência numérica: {frequencia_numérica:.3f} Hz")
print(f"Frequência analítica: {frequencia_analitica:.3f} Hz")


plt.plot(t, x)
plt.title("Movimento harmónico simples")
plt.xlabel("t(s)")
plt.ylabel("x(m)")
plt.plot(tempos[i], amplitude_analitica, marker="o", color="red", 
         label="Amplitude máxima")
plt.legend(loc="upper left")
plt.show()