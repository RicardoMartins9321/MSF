import numpy as np
import matplotlib.pyplot as plt

# parámetros e condições iniciais
con=np.pi/180.
phi=35
theta=90.-phi
phi=phi*con
theta=theta*con
det=-np.cos(theta)*np.sin(phi)-np.sin(theta)*np.cos(phi)
vaz=-np.sin(phi)/det
vam=-np.cos(phi)/det
v2=vaz**2+vam**2

print('det, vaz, vam, vaz**2 + vam**2 = ', det,vaz,vam,v2)

a=np.array([[np.cos(theta), np.cos(phi)], [np.sin(theta), -np.sin(phi)]])
b=np.array([1,0])

x = np.linalg.solve(a, b)
print(x)