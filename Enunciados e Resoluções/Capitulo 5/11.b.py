import numpy as np
import matplotlib.pyplot as plt

v = 40/3.6
m = 75
Cres = 0.9
A = 0.3
p = 1.225
u = 0.004
g = 9.8


P = u*m*g*v + (Cres/2)*A*p*(v**2)*v
P_cavalos = P/735.4987
print(f"{P:.0f} W = {P_cavalos:.3f} cv")
