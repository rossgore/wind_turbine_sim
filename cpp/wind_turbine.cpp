#include "wind_turbine.h"
#include <cmath>

// Constants
const double speed_norm = 1.2;
const double beta = 0;
const double kp = 0.73;
const double Lambda_nom = 8.1;
const double Pmw_base = 1.5e6;
const double epsilon = 1e-6;

double calculate_power_output(double Vw, double ww_pu) {
    double Vw_pu = Vw / 12.0;
    
    double Lambda = (ww_pu / speed_norm) / Vw_pu * Lambda_nom;
    
    double Lambda_i = 1.0 / (1.0 / (Lambda + 0.08 * beta) - 0.035 / (std::pow(beta, 3) + 1));
    
    double Cp = 0.5176 * (116.0 / Lambda_i - 0.4 * beta - 5) * std::exp(-21.0 / Lambda_i) + 0.0068 * Lambda;
    double Cp_pu = Cp / 0.48;
    
    double Pmw_pu = kp * Cp_pu * std::pow(Vw_pu, 3);
    
    // Check if Pmw_pu is less than 0, return 0 if true
    if (Pmw_pu < 0) {
        return 0;
    }
    
    return Pmw_pu;
}
