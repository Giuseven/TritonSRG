from Solvers import Solvers
from PlotandAnalysis import Switchers
from Checks import Checks
import os

# Let you choose the evolution parameters

def UserValues():
    Bool = False
    Bool1= False
    while Bool == False:
        n_step = input("Enter the number of steps: ")
        Bool = Checks.checkIntPositive1(n_step)

    while Bool1 == False:
        s_f = input("Enter the final value of the evolution parameter s: ")
        Bool1 = Checks.checkFloatPositive(s_f)
    ds = float(s_f) / int(n_step)
    print("The value of each step is: ", round(ds, 5))
    return int(n_step), float(s_f), round(ds,5)


# Main switcher of the project, let you choose the method to solve the SRG or enters the analysis environment.
# You can re-enter to the analysis environment without being forced to perform the Solver routine all over again

def SRGSolver():
    print("You have entered the SRG solver environment!")
    AnalysisBool = False
    while True:
        print("Your options: \n Solve with Euler Method at first order (Type 'Euler')\n Solve with Gunge-Kutta method at 4-th order (Type 'GK4') \n Solve with Radau Method from Scipy (Type 'Radau') \n Solve with OdeInt routine from Scipy (Type 'OdeInt')  \n Enter the Analysis environment (Type 'Analysis') \n Exit this environment (Type 'exit')")
        choice = input("Enter your choice : ")

        if choice != 'Analysis':
            AnalysisBool = False

        if choice == 'Euler':
            n_step, s_f, ds = UserValues()
            HMatEV, VMatEV = Solvers.Euler(ds, n_step)
            LastChoice = 'Euler'
            AnalysisBool = Switchers.DoYouChooseAnalysis()

        if choice == 'GK4':
            n_step, s_f, ds = UserValues()
            HMatEV, VMatEV = Solvers.RKEvolution(ds, s_f)
            LastChoice = 'GK4'
            AnalysisBool = Switchers.DoYouChooseAnalysis()

        if choice == 'Radau':
            n_step, s_f, ds = UserValues()
            HMatEV, VMatEV = Solvers.RadauOdeInt(choice, n_step, s_f)
            LastChoice = 'Radau'
            AnalysisBool = Switchers.DoYouChooseAnalysis()

        if choice == 'OdeInt':
            n_step, s_f, ds = UserValues()
            HMatEV, VMatEV = Solvers.RadauOdeInt(choice, n_step, s_f)
            LastChoice = 'OdeInt'
            AnalysisBool = Switchers.DoYouChooseAnalysis()

        if choice == 'exit' :
            break

        if choice == 'Analysis' or AnalysisBool == True :
            try:
                HMatEV
            except NameError:
                print("I'm sorry but no evolved Hamiltonian is found, start a solver first")
            else:
                Switchers.AnalysisEnvironment(VMatEV, HMatEV, LastChoice, n_step, s_f, ds)
        
        else:
            _ = os.system('clear')
            print("Not a valid input, try again")