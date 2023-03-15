import numpy as np
import matplotlib.pyplot as plt

# Define an empty list to store the arrays
data = []

# Loop through each file and read in the data as a numpy array

#filename = f"Method1.dat"  # Change this to the actual filenames of your data files
#array = np.loadtxt(filename)
#data.append(array)
filename = f"Method1.dat"  # Change this to the actual filenames of your data files
array = np.loadtxt(filename)
data.append(array)
filename = f"Method3.dat"  # Change this to the actual filenames of your data files 
array = np.loadtxt(filename) 
data.append(array) 
#filename = f"Method2.dat"  # Change this to the actual filenames of your data files
#array = np.loadtxt(filename)
#data.append(array)
s = np.linspace(0, 0.5, 26)
# Plot the arrays
plt.plot(s,data[0], label='Euler')
plt.plot(s,data[1], label='Radau')
#plt.plot(data[2], label='Array 3')
#plt.plot(data[3], label='Array 4')

# Add labels and legend
plt.xlabel(r'Evolution parameter $s$')
plt.ylabel(r'Ground State $E_0$')
plt.legend()

# Display the plot
plt.show()
