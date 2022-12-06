import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys
import time

from scipy.integrate import odeint

# Set random seed (for reproducibility)
np.random.seed(41)

def HH(I):
    tmin = 0.0
    tmax = 100.0
    T = np.linspace(tmin, tmax-1, 5000)

    gK = 36.0 # Average potassium channel conductance per unit area (mS/cm^2)
    gNa = 120.0 # Average sodium channel conductance per unit area (mS/cm^2)
    gL = 0.3 # Average leak channel conductance per unit area (mS/cm^2)
    Cm = 1.0 # Membrane capacitance per unit area (uF/cm^2)
    VK = -12.0  # Potassium potential (mV)
    VNa = 115.0 # Sodium potential (mV)
    Vl = 10.613 # Leak potential (mV)

    # Potassium ion-channel rate functions
    def alpha_n(Vm): return (0.01 * (10.0 - Vm)) / (np.exp(1.0 - (0.1 * Vm)) - 1.0)
    def beta_n(Vm): return 0.125 * np.exp(-Vm / 80.0)

    # Sodium ion-channel rate functions
    def alpha_m(Vm): return (0.1 * (25.0 - Vm)) / (np.exp(2.5 - (0.1 * Vm)) - 1.0)
    def beta_m(Vm): return 4.0 * np.exp(-Vm / 18.0)
    def alpha_h(Vm): return 0.07 * np.exp(-Vm / 20.0)
    def beta_h(Vm): return 1.0 / (np.exp(3.0 - (0.1 * Vm)) + 1.0)
      
    # n, m, and h steady-state values
    def n_inf(Vm=0.0): return alpha_n(Vm) / (alpha_n(Vm) + beta_n(Vm))
    def m_inf(Vm=0.0): return alpha_m(Vm) / (alpha_m(Vm) + beta_m(Vm))
    def h_inf(Vm=0.0): return alpha_h(Vm) / (alpha_h(Vm) + beta_h(Vm))
      
    # Input stimulus
    def Id(t): return I[int(t)]
      
    def compute_derivatives(y, t0):
        dy = np.zeros((4,))
        
        Vm = y[0]
        n = y[1]
        m = y[2]
        h = y[3]
        
        # dVm/dt
        GK = (gK / Cm) * np.power(n, 4.0)
        GNa = (gNa / Cm) * np.power(m, 3.0) * h
        GL = gL / Cm
        
        dy[0] = (Id(t0) / Cm) - (GK * (Vm - VK)) - (GNa * (Vm - VNa)) - (GL * (Vm - Vl))
        dy[1] = (alpha_n(Vm) * (1.0 - n)) - (beta_n(Vm) * n) # dn/dt
        dy[2] = (alpha_m(Vm) * (1.0 - m)) - (beta_m(Vm) * m) # dm/dt
        dy[3] = (alpha_h(Vm) * (1.0 - h)) - (beta_h(Vm) * h) # dh/dt
        
        return dy
      
    Y = np.array([0.0, n_inf(), m_inf(), h_inf()]) # (Vm, n, m, h)

    # Solve ODE system
    Vy = odeint(compute_derivatives, Y, T)

    Idv = [Id(t) for t in T] 

    return T, Idv, Vy 


if __name__ == "__main__":
    DF = pd.read_csv('data_seq.csv', sep = ',', header = None, index_col=0) #, skiprows = lambda x: x % 2 )
    input_char = sys.argv[1]
    letter = DF.loc[list(DF.index == input_char),:].to_numpy()

    if len(letter) > 1: letter = letter[int(sys.argv[2])].reshape(3,-1)*10
    else: letter = letter.reshape(3,-1)*10

    for row in range(3):
        I = letter[row]

        T, Idv, Vy = HH(I)

        fig, (ax1, ax2) = plt.subplots(1,2,figsize=(25, 4))
        ax1.plot(T, Idv)
        ax1.set_ylim(0,10)
        ax1.set_xlabel('Time (ms)')
        ax1.set_ylabel(r'Current density (uA/$cm^2$)')
        ax1.set_title('Stimulus (Current density)')
        plt.grid()

        # Neuron potential
        ax2.plot(T, Vy[:, 0])
        ax2.set_ylim(-15,110)
        ax2.set_xlabel('Time (ms)')
        ax2.set_ylabel('Vm (mV)')
        ax2.set_title('Neuron potential')
        plt.grid()

        plt.tight_layout()
        plt.savefig(f'./hh_{row}.png',bbox_inches='tight', dpi=300)
