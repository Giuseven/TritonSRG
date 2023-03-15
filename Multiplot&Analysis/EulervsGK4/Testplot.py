import numpy as np
import matplotlib.pyplot as plt

# Define an empty list to store the arrays
data = []
data1 = []

# Loop through each file and read in the data as a numpy array

#filename = f"GK4_sfinal_0.1_nsteps_500_NGround_25.dat"  # Change this to the actual filenames of your data files
#array = np.loadtxt(filename)
#data.append(array)
filename = f"GK4_sfinal_0.5_nsteps_1000_NGround_25.dat"  # Change this to the actual filenames of your data files
array = np.loadtxt(filename)
data.append(array)
#filename = f"GK4_sfinal_1.0_nsteps_1000_NGround_25.dat"  # Change this to the actual filenames of your data files 
#array = np.loadtxt(filename) 
#data.append(array) 
#filename = f"GK4_sfinal_2.5_nsteps_1000_NGround_25.dat"  # Change this to the actual filenames of your data files
#array = np.loadtxt(filename)
#data.append(array)
#filename = f"GK4_sfinal_5.0_nsteps_1000_NGround_25.dat"  # Change this to the actual filenames of your data files
#array = np.loadtxt(filename)
#data.append(array)
#filename = f"OdeInt_sfinal_0.1_nsteps_500_NGround_25.dat"  # Change this to the actual filenames of your data files
#array = np.loadtxt(filename)
#data1.append(array)
filename = f"1000steps.dat"  # Change this to the actual filenames of your data files
array = np.loadtxt(filename)
data1.append(array)
#filename = f"OdeInt_sfinal_1.0_nsteps_1000_NGround_25.dat"  # Change this to the actual filenames of your data files 
#array = np.loadtxt(filename) 
#data1.append(array) 
#filename = f"OdeInt_sfinal_2.5_nsteps_1000_NGround_25.dat"  # Change this to the actual filenames of your data files
#array = np.loadtxt(filename)
#data1.append(array)
#filename = f"OdeInt_sfinal_5.0_nsteps_1000_NGround_25.dat"  # Change this to the actual filenames of your data files
#array = np.loadtxt(filename)
#data1.append(array)
s = np.linspace(0, 0.5, 26)
# Plot the arrays
#plt.plot(s,data[0], label=r'GK4 $s_f = 0.5$')
#plt.plot(s,data[1], label=r'GK4 $s_f = 0.5$')
#plt.plot(s,data[2], label=r'GK4 $s_f = 1.0$')
#plt.plot(s,data[3], label=r'GK4 $s_f = 2.5$')
#plt.plot(s,data[4], label=r'GK4 $s_f = 5.0$')
plt.plot(s,data1[0], label=r'Euler $s_f = 0.5$')
#plt.plot(s,data1[1], label=r'OdeInt $s_f = 0.5$')
#plt.plot(s,data1[2], label=r'OdeInt $s_f = 1.0$')
#plt.plot(s,data1[3], label=r'OdeInt $s_f = 2.5$')
#plt.plot(s,data1[4], label=r'OdeInt $s_f = 5.0$')
#plt.yscale('log')
# Add labels and legend
plt.xlabel(r'Evolution parameter $s$',size = 13)
plt.ylabel(r'Ground State $E_0$ [MeV]',size = 13)
plt.title(r'')
plt.legend()

# Display the plot
plt.show()
