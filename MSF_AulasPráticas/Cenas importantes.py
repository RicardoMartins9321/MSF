import numpy as np
from matplotlib import pyplot as plt
import sympy as sym
from mpl_toolkits import mplot3d
from numpy import linalg as LA

def aproxRet(f,n,dx):
    #realiza a aproximação regular de uma função
    return dx*np.sum(f[0:n])

def aproxTrap(f,n,dx):
    #realiza a aproximação trapezoidal de uma função
    return dx*(0.5*(f[0]+f[n])+np.sum(f[1:n]))