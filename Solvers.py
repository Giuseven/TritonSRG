import numpy as np
from scipy.integrate import solve_ivp, odeint
import time

class Constants:

    hbarc = 197.327053
    MN0 = (938.27231 + 939.56563) / 2
    MN = MN0 / (hbarc**2)
    TMat = np.loadtxt('kinetic_EMax20_hw20.dat')
    VMat = np.loadtxt('chi2b3b_EMax20_hw20.dat')
    HMat0 = TMat + VMat

class Solvers:
    
    # Class of all the available algorithm to solve the RGEs, first the RH side of the equation is defined, then solved

    def RightHand_2D(s, HMat):
        return Constants.MN**2 * (np.matmul(np.matmul(Constants.TMat, HMat), HMat) - 2 * np.matmul(np.matmul(HMat, Constants.TMat), HMat) + np.matmul(np.matmul(HMat, HMat), Constants.TMat))

    def RightHand_1D(y, s):
        HMat = np.reshape(y, (632, 632))
        HMatDel = Solvers.RightHand_2D(s,HMat)
        return HMatDel.flatten()
    
    def Euler(Del, n):
        s=0
        print("Initializing the evolution...")
        HMat_s= []
        VMat_s= []
        HMat = np.copy(Constants.HMat0)
        HMat_s.append(HMat)
        VMat_s.append(Constants.VMat)
        start_time= time.time()
        for i in range(n):
            HMatDel = Del * Solvers.RightHand_2D(s, HMat)
            HMat = HMat + HMatDel
            s = round(s + round(Del,5),5)
            print("\033[F\033[K", end="")
            print("Successfully evolved up to s = ", s,"/",round(n*Del,5))
            HMat_s.append(HMat)
            VMat_s.append(HMat-Constants.TMat)
        print("\033[F\033[K", end="")
        end_time=time.time()
        print(f'Done! Evolution completed in {end_time-start_time} s')
        return HMat_s, VMat_s

    def RungeKutta4(s, HMat, ds):
        k1 = ds * Solvers.RightHand_2D(s, HMat)
        k2 = ds * Solvers.RightHand_2D(s + ds/2, HMat + k1/2)
        k3 = ds * Solvers.RightHand_2D(s + ds/2, HMat + k2/2)
        k4 = ds * Solvers.RightHand_2D(s + ds, HMat + k3)
        return HMat + (k1 + 2*k2 + 2*k3 + k4) / 6

    def RKEvolution(ds, s_f):
        print("Initializing the evolution...")
        HMat_s=[]
        VMat_s=[]
        HMat= Constants.HMat0
        HMat_s.append(HMat)
        VMat_s.append(Constants.VMat)
        s=0
        start_time= time.time()
        while s < s_f:
            HMat = Solvers.RungeKutta4(s, HMat, ds)
            s = s + round(ds,5)
            s = round(s, 5)
            print("\033[F\033[K", end="")
            print("Successfully evolved up to s = ", s,"/",s_f)
            HMat_s.append(HMat)
            VMat_s.append(HMat-Constants.TMat)
        print("\033[F\033[K", end="")
        end_time=time.time()
        print(f'Done! Evolution completed in {end_time-start_time} s')
        return HMat_s, VMat_s
    
    def RadauOdeInt(choice, n_step, s_f):
        s= np.linspace(0, s_f, n_step+1)
        print("Evolving up to s =",s_f,"...")
        start_time= time.time()
        if choice == 'Radau':
            sol = solve_ivp(fun=lambda s, HMat: Solvers.RightHand_1D(HMat, s), t_span=[s[0], s[-1] ], y0=(Constants.HMat0).flatten(), t_eval=s)
            Radausol = sol.y.reshape(632, 632, len(s))
            HMat_s = [Radausol[:, :, i] for i in range(len(s))]
        if choice == 'OdeInt':
            sol = odeint(Solvers.RightHand_1D,(Constants.HMat0).flatten() , s)
            HMat_s = sol.reshape(len(s), 632, 632)
        print("\033[F\033[K", end="")
        end_time=time.time()
        print(f'Done! Evolution completed in {end_time-start_time} s')
        VMat_s = [(HMat_s[i]-Constants.TMat) for i in range(len(s))]
        return HMat_s, VMat_s
    