import numpy as np

# Constants
speed_norm = 1.2
beta = 0
kp = 0.73
Lambda_nom = 8.1
Pmw_base = 1.5e6
epsilon = 1e-6

def calculate_power_output(Vw, ww_pu):
    Vw_pu = Vw / 12
    
    Lambda = (ww_pu / speed_norm) / Vw_pu * Lambda_nom
    
    Lambda_i = 1 / (1 / (Lambda + 0.08 * beta) - 0.035 / (beta**3 + 1))
    
    Cp = 0.5176 * (116 / Lambda_i - 0.4 * beta - 5) * np.exp(-21 / Lambda_i) + 0.0068 * Lambda
    Cp_pu = Cp / 0.48
    
    Pmw_pu = kp * Cp_pu * Vw_pu**3
    
    # Return 0 if Pmw_pu is less than zero
    if Pmw_pu < 0:
        return 0
    
    return Pmw_pu
