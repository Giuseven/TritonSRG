import SRGSolver
from PlotandAnalysis import Plots
from Solvers import Constants
import os

##################################################################################################
#                                                                                                #
#          SRG Solver for Theoretical and Numerical Aspects of Nuclear Physics Project           #
#                                                                                                #
#                               Author: Giuseppe Ventura                                         #
#                                                                                                #
#                                                                                                #
##################################################################################################       


def main():
    print("Welcome! This is Giuseppe Ventura's project for Theoretical and Numerical Aspects of Nuclear Physics")
    
    while True:
        print("You can choose among some options: \n 1) Start the SRG Solver Environment (Type '1' or 'SRG')\n 2) Plot the initial datas (Type '2' or 'Plot') \n 3) Exit the program (Type '3' or 'exit')")
        FirstChoice = input("Your choice: ")
        if FirstChoice == '1' or FirstChoice == 'SRG':
            SRGSolver.SRGSolver()
            Bool = True
        if FirstChoice == '2' or FirstChoice == 'Plot':
            Plots.PlotInitialDatas(Constants.TMat, Constants.VMat)
        if FirstChoice == '3' or FirstChoice == 'exit':
            break
        else:
            _ = os.system('clear')
            pass

if __name__ == '__main__':
    main()