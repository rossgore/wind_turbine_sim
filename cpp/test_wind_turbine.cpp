#include <iostream>
#include <iomanip>
#include <vector>
#include "wind_turbine.h" // Assume this header contains the calculate_power_output declaration

// Constants for the test
const int NUM_VW_VALUES = 6;
const int NUM_WW_PU_VALUES = 61;

void run_tests() {
    std::vector<double> Vw_values = {5, 7, 8, 10, 12, 14};
    std::vector<double> ww_pu_values(NUM_WW_PU_VALUES);
    
    // Generate ww_pu_values (equivalent to np.arange(0, 3.05, 0.05))
    for (int i = 0; i < NUM_WW_PU_VALUES; i++) {
        ww_pu_values[i] = i * 0.05;
    }

    for (const auto& Vw : Vw_values) {
        std::cout << "\nWind Speed (Vw): " << std::fixed << std::setprecision(1) << Vw << " m/s\n";
        std::cout << "Generator Speed (ww_pu) | Power Output (Pmw_pu)\n";
        std::cout << "---------------------------------------------\n";
        
        for (const auto& ww_pu : ww_pu_values) {
            double Pmw_pu = calculate_power_output(Vw, ww_pu);
            std::cout << std::fixed << std::setprecision(2) << ww_pu << " | " 
                      << std::fixed << std::setprecision(4) << Pmw_pu << "\n";
        }
    }
}

int main() {
    run_tests();
    return 0;
}
