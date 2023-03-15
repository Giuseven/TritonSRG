import numpy as np
import matplotlib.pyplot as plt


data = []


filename = f"100steps.dat"  
array = np.loadtxt(filename)
data.append(array)
filename = f"500steps.dat" 
array = np.loadtxt(filename)
data.append(array)
filename = f"1000steps.dat"  
array = np.loadtxt(filename) 
data.append(array) 
filename = f"2000steps.dat"  
array = np.loadtxt(filename)
data.append(array)
s = np.linspace(0, 0.5, 26)
# Plot the arrays
plt.plot(s,data[0], label='100' ,  linestyle='-',linewidth=2)
plt.plot(s,data[1], label='500' ,  linestyle='-', linewidth=2)
plt.plot(s,data[2], label='1000',  linestyle='-', linewidth=2)
plt.plot(s,data[3], label='2000' ,  linestyle='-', linewidth=2)
#plt.plot(s,data[0], 'o',color='black', markersize=3)
#plt.plot(s,data[1], 'o',color='black', markersize=3)
#plt.plot(s,data[2],'o',color='black', markersize=3)
#plt.plot(s,data[3], 'o',color='black', markersize=3)


plt.xlabel(r'Evolution parameter $s$',size = 13)
plt.ylabel(r'Ground State $E_0$ [MeV]',size = 13)
plt.title(r'SRG evolution with Euler method')
plt.legend()


plt.show()
