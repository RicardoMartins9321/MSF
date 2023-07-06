import numpy as np
import matplotlib.pyplot as plt


plt.figure("Vetores")
def formula_movimento(t): 
    return 2*t, t**2

x0 = 0
y0 = 0

plt.subplot(1,2,1)
t = 1
xa, ya = formula_movimento(t)
plt.arrow(x0,y0,xa,ya,color='red',width=0.1, label="Vetor A")

t = 2
xb, yb = formula_movimento(t)
plt.arrow(x0,y0,xb,yb,color='orange',width=0.1, label="Vetor B")

t = 3
xc, yc = formula_movimento(t)
plt.arrow(x0,y0,xc,yc,color='green',width=0.1, label="Vetor C")

t = 4
xd, yd = formula_movimento(t)
plt.arrow(x0,y0,xd,yd,color='blue',width=0.1, label="Vetor D")

plt.axis("equal") # makes it so all the vetors are equal in size
plt.title("Vetores correto")
plt.legend()


plt.subplot(1,2,2)
t = 1
xa, ya = formula_movimento(t)
plt.arrow(x0,y0,xa,ya,color='red',width=0.1, label="Vetor A")

t = 2
xb, yb = formula_movimento(t)
plt.arrow(xa,ya,xb,yb,color='orange',width=0.1, label="Vetor B")

t = 3
xc, yc = formula_movimento(t)
plt.arrow(xb,yb,xc,yc,color='green',width=0.1, label="Vetor C")

t = 4
xd, yd = formula_movimento(t)
plt.arrow(xc,yc,xd,yd,color='blue',width=0.1, label="Vetor D")


plt.axis("equal") # makes it so all the vetors are equal in size
plt.title("Vetores incorreto")
plt.legend()
plt.show()