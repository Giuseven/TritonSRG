import numpy as np
import matplotlib.pyplot as plt
import os
from Checks import Checks

# List of functions used in the program for plotting, analyzing and saving the results obtained by the RGE

class Plots:

    # Plot class: all the functions used to plot stuff, functions names are self-explanatory for their purpose
    # Plots can be saved automatically to a file, the storing is automatically managed 

    def PlotInitialDatas(TMat,VMat):
        fig, axes = plt.subplots(1,2, figsize=(18,12))
        im1= axes[0].imshow(np.abs(TMat), extent=[0, TMat.shape[1], 0, TMat.shape[0]],cmap='summer_r', vmin=0, vmax=3)
        axes[0].set_title('Initial kinetic matrix')
        im2= axes[1].imshow(np.abs(VMat), extent=[0, VMat.shape[1], 0, VMat.shape[0]],cmap='summer_r', vmin=0, vmax=3)
        axes[1].set_title("Initial potential matrix")
        plt.show()

    def PlotAnSaveEvolvedPotentials(VMatEV, n_step, ds, choice):
        a=0
        Bool = False
        while Bool == False:
            Nplot = input("How many plots do you want? (Default=5):")
            if Nplot == '':
                Nplot = 5
                break
            Bool = Checks.checkIntPositive(Nplot, n_step)
        Nplot = int(Nplot)
        k= n_step / Nplot
        s_f = round(n_step*ds,5)
        k = round(k)
        # Create folder to store the saved plots
        while True:
            save = input("Do you want to save the plots on the disk? (y/n):")
            if save == 'y':
                Folder = "SavedPlots/{}/S_final_{}/N_steps_{}".format(choice,s_f,n_step)
                if not os.path.exists(Folder):
                    os.makedirs(Folder)
                break
            if save == 'n':
                break
            else:
                print("Not a valid input.")
        # Plots and save the evolved Potentials
        i = 0
        j = 0
        while i <= Nplot+1 and j <= n_step+1 :
            plt.imshow(np.abs(VMatEV[j]), extent=[0, VMatEV[j].shape[1], 0, VMatEV[j].shape[0]],cmap='summer_r', vmin=0, vmax=3)
            plt.title("Potential evolved up to s={}".format(a))
            plt.colorbar()
            if save == 'y':
                plt.savefig("SavedPlots/{}/S_final_{}/N_steps_{}/Plot_s_{}.png".format(choice, s_f, n_step, a))
            plt.show()
            i = i + 1
            j = j + k
            a = a + (k*round(ds,5))
            a= round(a,5)

    def PlotGroundStates(GroundStates, choice, s_f, variable, n_step, GroundChoice):

        while True:
            save = input("Do you want to save the plot on the disk? (y/n):")
            if save == 'y':
                Folder = "SavedPlots/Groundstates/{}".format(choice)
                if not os.path.exists(Folder):
                    os.makedirs(Folder)
                break
            if save == 'n':
                break
            else:
                print("Not a valid input.")
        s= np.linspace(0, s_f, variable+1)
        if len(s) != len(GroundStates):
            i = 0
            while True:
                s= np.linspace(0, s_f, variable+i)
                if len(s) == len(GroundStates):
                    break
                s = np.linspace(0, s_f, variable-i)
                if len(s) == len(GroundStates):
                    break
                i = i+1
        plt.plot(s, GroundStates)
        plt.title("Ground States of H(s) as function of s")
        plt.xlabel("Flow parameter s")
        plt.ylabel("E_0")
        if save == 'y':
            plt.savefig("SavedPlots/Groundstates/{}/GroundStates_sf_{}_nsteps_{}_NGround_{}.png".format(choice, s_f, n_step, variable))
        plt.show()

class GroundStateCompute:
    
    # A function that computes the ground state for the evolved potential, we can \ 
    # choose how many do we want to compute, they will automatically distributed so\
    # that they cover the full evolution
    
    def Groundstate(GroundChoice, HMatEV, n_step):
        Eigvalues = []
        Ground_state_s = []
        if GroundChoice == 1:
            Bool = False
            while Bool == False:
                NGroundState = input("How many groundstates do you want to compute? :")
                Bool = Checks.checkIntPositive(NGroundState, n_step)
            NGroundState = int(NGroundState)
            k = n_step / NGroundState
            k = round(k)
        if GroundChoice == 2:
            NGroundState = n_step
            k = 1
        print("Computing {} ground states...".format(NGroundState))
        i = 0
        j=0
        while i <= n_step:
            if len(Ground_state_s) <= NGroundState+1:
                Eigvalues.append(np.linalg.eigvals(HMatEV[i]))
                Ground_state_s.append(np.min(Eigvalues[j]))
            i = i + k
            j = j + 1
        print("\033[F\033[K", end="")
        print("Done!")
        return Ground_state_s, NGroundState, k
    

class Switchers:

    # A class that groups together all the functions that allow us to make choice within the program

    def AnalysisEnvironment(VMatEV, HMatEV, choice, n_step, s_f, ds):
        while True:
            print("You are in the analysis enviroment for the last method you used: the {} method! \n 1) Compute and study the Ground state of the Hamiltonian vs the flow parameter \n 2) Plot the Evolved Potential for different values of the flow parameters \n 3) Write the Evolved potentials or Hamiltonian for different values of the flow parameter s \n 4) Exit this enviroment".format(choice))           
            AnalysisChoice = input("Your choice (1/4): ")
            if AnalysisChoice == '1':
                Switchers.EigenvalueSwitcher(HMatEV, n_step, ds, choice)
            if AnalysisChoice == '2':
                Plots.PlotAnSaveEvolvedPotentials(VMatEV, n_step, ds, choice)
            if AnalysisChoice == '3':
                Switchers.WriteOnFileSwitcher(VMatEV, ds, n_step, choice)
            if AnalysisChoice == '4':
                break
            else:
                print("Not a valid input")

    def DoYouChooseAnalysis():
        while True:
            Choice = input("Do you want to enter the Analysis environment? (y/n) :")
            if Choice == 'y':
                A = True
                break
            if Choice == 'n':
                A = False
                break
            else:
                print("Not a valid input")
        return A

    def WriteOnFileSwitcher(VMatEV, ds, n_step, choice):
        print("Would you like to... \n 1) Choose the number of files to write on the disk \n 2) Write for all the values of s computed (Takes a lot of time for large numbers of steps)")
        while True:
            WriteChoice = input("Type the answer (1/2)")
            if WriteChoice == '1':
                NFiles, k = WriteOnFile.SaveFiniteChoice(n_step)
                variable= NFiles
                WriteOnFile.SaveEvolvedPotentials(VMatEV, ds, n_step, choice, variable, k)
                break

            if WriteChoice == '2':
                variable = n_step+1
                k=1
                WriteOnFile.SaveEvolvedPotentials(VMatEV, ds, n_step, choice, variable,k)
                break

            else:
                print("Not a valid input")



    def EigenvalueSwitcher(HMatEV, n_step, ds, choice):

        s_f = round(n_step*ds,5)
        print("Would you like to... \n 1) Choose the number of Ground states to compute (Type '1') \n 2) Compute all the possible ground states (Requires a lot of time for big number of steps, currently {}) (Type '2')".format(n_step))
        while True:
            inp = input("Type the answer (1/2):")
            if inp == '1':
                GroundStates, NGroundStates, k = GroundStateCompute.Groundstate(int(inp), HMatEV, n_step)
                break
            if inp == '2':
                GroundStates, NGroundStates, k = GroundStateCompute.Groundstate(int(inp), HMatEV, n_step)
                break
            else:
                print("Not a valid input")

        while True:
            print("What do you want to do with the Ground states of the evolved Hamiltonians? : \n 1) Print them for every value of s \n 2) Plot them vs s \n 3) Save them in a file \n 4) Exit the Ground State environment ")
            bool = False
            while bool == False:
                EigChoice = input("Your choice (1/4): ")
                bool = Checks.checkIntPositive1(EigChoice)
            EigChoice = int(EigChoice)
            if EigChoice == 1 :
                print(GroundStates)             
            if EigChoice == 2:
                Plots.PlotGroundStates(GroundStates, choice, s_f,NGroundStates, n_step, int(inp))         
            if EigChoice == 3:
                WriteOnFile.SaveGroundStates(GroundStates, choice, s_f, n_step, NGroundStates)
            if EigChoice == 4:
                break
            if EigChoice > 4:
                print("Not a valid choice!")


class WriteOnFile:
    # A class that groups all the routines that write datas on a file

    def SaveFiniteChoice(n_step):    
        Bool = False
        while Bool == False:
            NFiles= input("How many files do you want to create?:")
            Bool = Checks.checkIntPositive(NFiles, n_step)
        NFiles = int(NFiles)
        k= n_step / NFiles
        k = round(k)
        return NFiles, k

    def SaveEvolvedPotentials(VMat, ds, n_step, choice, variable,k):
        s_f = round(n_step*ds,5)
        print("Exporting the Evolved Potentials to: EvolvedPotentials/{}/Sfinal_{}_Nsteps_{}_NFiles_{} ...".format(choice, s_f, n_step, variable))
        Folder = "EvolvedPotentials/{}/Sfinal_{}_Nsteps_{}_NFiles_{}".format(choice, s_f, n_step, variable)
        if not os.path.exists(Folder):
            os.makedirs(Folder)
        j = 0
        a = 0
        while j <= n_step+1 :
            filename="EvolvedPotentials/{}/Sfinal_{}_Nsteps_{}_NFiles_{}/EvolvedPotential_s_{}.dat".format(choice, s_f, n_step,variable, a)
            with open(filename, "w") as file:
                for row in VMat[j]:
                    file.write(" ".join(str(x) for x in row))
                    file.write("\n")
            j = j+k
            a = round(a + round(k*ds,5),5)
        print("Done!")

    def SaveGroundStates(GroundStates, choice, s_f, n_step, variable):
        print("Exporting the Ground states to: GroundStates/{} ...".format(choice))
        Folder = "Groundstates/{}".format(choice)
        if not os.path.exists(Folder):
            os.makedirs(Folder)
        FileName = "GroundStates_sfinal_{}_nsteps_{}_NGround_{}.dat".format(s_f,n_step,variable)
        FilePath = os.path.join(Folder, FileName)
        with open(FilePath, "w") as file:
            for element in GroundStates:
                file.write(str(element) + "\n")
        print("Done!")