import numpy as np
import matplotlib.pyplot as plt

def y_function(x):
    return np.sin(x)

def y_derivative(x):
    return np.cos(x)

x = np.arange(-5, 5, 0.1)
y = y_function(x)

current_pos = (1.5, y_function(1.5))

# How fast we want to move to the minimum
learning_rate = 0.01

plt.ion()  

for _ in range(1000):
    plt.clf()  
    
    new_x = current_pos[0] - learning_rate * y_derivative(current_pos[0])
    new_y = y_function(new_x)
    current_pos = (new_x, new_y)
    
   
    plt.plot(x, y)
    plt.scatter(current_pos[0], current_pos[1], color="red")
    plt.pause(0.001)  

plt.ioff()  
plt.show()  


