import numpy as np                  # reducing the name to np for easier  use
import matplotlib.pyplot as plt     # reducing the name to plt for easier use

#plt.style.use("dark_background")    # choose the style for everything
#plt.style.use("classic")
#plt.style.use("ggplot")

# Compute the x and y coordinates for points on a sine curve 
x = np.arange(0, 3 * np.pi, 0.1) 
y_sin = np.sin(x)
y_cos = np.cos(x)

# .arange(start, end, step) -   creates a numpy array; 
#                               smaller the step the smoother the graphic 

# Plot the points using matplotlib 
plt.figure("Sine", figsize=(8,5))  # name / width and height of the page 
plt.plot(x, y_sin)  # plots the graphic
plt.title("sine wave form") # title of the graphic
plt.xlabel("Tempo(s)")  # xlabel
plt.ylabel("Amplitude") # ylabel

plt.figure("Cossine")
plt.plot(x, y_cos)
plt.grid()
plt.title("Cossine wave form")
plt.xlabel("Tempo(s)")
plt.ylabel("Amplitude")

plt.xlim(2, 8)  # set the x limites
plt.ylim(0,1.5) # set the y limits

# [x1 to x2], [y1 to y2]
plt.plot([0, 6.25], [1, 1] , color="black", linestyle="--", lw="1.5")  
plt.plot([6.25, 6.25], [0, 1], color="black", linestyle="--", lw="1.5")

plt.plot(6.25, 1, marker="x", color="r", markersize=10) # create a marker
plt.text(6.25, 1.05, "P(6.25, 1.00)")

plt.text(5, 0.5, "cos(x)", bbox=dict(facecolor="red", alpha=0.5), fontsize=10)

plt.annotate("P(6.25, 1.00)", xy=(6.25, 1.0), fontsize=16, xytext=(2.5, 0.5),
             arrowprops=dict(facecolor="red"), color="green")

# .show() shows all the graphics that were plotted up to that point
plt.show()


import numpy as np 
import matplotlib.pyplot as plt  
   
# Compute the x and y coordinates for points on sine and cosine curves 
x = np.arange(0, 3 * np.pi, 0.1) 
y_sin = np.sin(x) 
y_cos = np.cos(x)  
   
# Use this to directly adjust the subplots display
plt.subplots_adjust(hspace=0.5)

# Set up a subplot grid that has height 2 = 2 rows and width 1 = 1 column, 
# and set the first such subplot as active.
# .subplot(row, column, position) 
plt.subplot(2, 2, 1)
   
# Make the first plot 
plt.plot(x, y_sin, color="r")
plt.grid() 
plt.title('Sine')  

   
# Set the second subplot as active, and make the second plot. 
# Set everything the same and you create a graphic on top of one another
plt.subplot(2, 2, 2) 
plt.plot(x, np.cos(x*3), color="g") 
plt.title('Cossine * 3')  
   
plt.subplot(2, 2, 3) 
plt.plot(x, y_cos, lw=5)  # lw é a espessura da linha, 1.0 é o valor padrão
plt.title('Cossine') 

plt.subplot(2, 2, 4) 
plt.plot(x, y_cos, marker=".")
plt.title('Cossine')

plt.subplot(2, 2, 4)   
plt.plot(x, y_sin, linestyle="-.") 
plt.title('Cossine and Sine')  

# Show the figure. 
plt.show()
