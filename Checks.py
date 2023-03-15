# Routines that check whether the user choices are compatible with the program needs or make sense within the environment

class Checks:
    def checkIntPositive(inp, nstep):
        try:
            inp = int(inp)
            if inp > 0 :
                if inp > nstep:
                    print("This value exceeds the maximum which is :",nstep)
                    Bool = False
                    return Bool
                else:
                    Bool = True
                    return Bool
            else:
                print("Not a valid positive integer!")
                Bool = False
                return Bool
        except:
            print("The entered value is not an integer!")
            Bool = False
            return Bool
        
    def checkIntPositive1(inp):
        try:
            inp = int(inp)
            if inp > 0 :
                Bool = True
                return Bool
            else:
                print("Not a valid positive integer!")
                Bool = False
                return Bool
        except:
            print("The entered value is not an integer!")
            Bool = False
            return Bool

    def checkFloatPositive(inp):
        try:
            inp = float(inp)
            if inp > 0 :
                Bool = True
                return Bool
            else:
                print("Not a positive number!")
                Bool = False
                return Bool
        except:
            print("The entered value is not a number!")
            Bool = False
            return Bool