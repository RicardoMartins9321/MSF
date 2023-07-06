import numpy as np
import matplotlib.pyplot as plt


plt.figure("Vetores")
# a)
x0 = 0
y0 = 0
xa = 0
ya = 5.0
plt.arrow(x0,y0,xa,ya,color='red',width=0.1, label="Vetor A")

# b)
xb = 2.5
yb = 4.33
plt.arrow(x0,y0,xb,yb,color='orange',width=0.1, label="Vetor B")

# c)
xc = -4.33
yc = 2.5
plt.arrow(x0,y0,xc,yc,color='green',width=0.1, label="Vetor C")

# d)
xd = 3.21
yd = -3.83
plt.arrow(x0,y0,xd,yd,color='blue',width=0.1, label="Vetor D")


plt.axis("equal") # makes it so all the vetors are equal in size
plt.title("Vetores")
plt.legend()
plt.show()