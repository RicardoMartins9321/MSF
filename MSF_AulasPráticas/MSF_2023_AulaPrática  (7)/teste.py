import numpy as np
import matplotlib.pyplot as plt

# Constants
v0 = 130 / 3.6  # initial velocity in m/s
theta = np.deg2rad(10)  # initial angle in radians
m = 0.057  # mass in kg
d = 0.067  # diameter in m
A = np.pi * (d/2)**2  # cross-sectional area in m^2
rho = 1.2  # air density in kg/m^3
Cd = 0.5  # drag coefficient
g = 9.81  # acceleration due to gravity in m/s^2
vt = np.sqrt((2 * m * g) / (rho * Cd * A))  # terminal velocity in m/s

# Time array
t = np.linspace(0, 10, 1000)  # time from 0 to 10 seconds

# Equations of motion
x = v0 * np.cos(theta) * t
y = v0 * np.sin(theta) * t - (1/2) * g * t**2

# Find the index where the ball hits y=0
idx = np.where(y <= 0)[0][0]

# Calculate the range and maximum height
R = x[idx]
ymax = (v0**2 * np.sin(theta)**2) / (2 * g)

# Plot the trajectory
plt.plot(x[:idx], y[:idx], label='Trajectory')
plt.plot([x[0], x[idx]], [0, 0], '--', label='Ground')
plt.plot(x[idx], y[idx], 'ro', label='Impact')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.title('Trajectory of a Tennis Ball (No Spin)')
plt.legend()
plt.show()

# Print the range and maximum height
print('Range: {:.2f} m'.format(R))
print('Maximum height: {:.2f} m'.format(ymax))
