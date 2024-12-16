#include <stdio.h>
#include <math.h>

// Include the function declaration
double calculate_power_output(double Vw, double ww_pu);

// Constants for the test
#define NUM_VW_VALUES 6
#define NUM_WW_PU_VALUES 61

void run_tests() {
    double Vw_values[NUM_VW_VALUES] = {5, 7, 8, 10, 12, 14};
    double ww_pu_values[NUM_WW_PU_VALUES];
    
    // Generate ww_pu_values (equivalent to np.arange(0, 3.05, 0.05))
    for (int i = 0; i < NUM_WW_PU_VALUES; i++) {
        ww_pu_values[i] = i * 0.05;
    }

    for (int i = 0; i < NUM_VW_VALUES; i++) {
        double Vw = Vw_values[i];
        printf("\nWind Speed (Vw): %.1f m/s\n", Vw);
        printf("Generator Speed (ww_pu) | Power Output (Pmw_pu)\n");
        printf("---------------------------------------------\n");
        
        for (int j = 0; j < NUM_WW_PU_VALUES; j++) {
            double ww_pu = ww_pu_values[j];
            double Pmw_pu = calculate_power_output(Vw, ww_pu);
            printf("%.2f | %.4f\n", ww_pu, Pmw_pu);
        }
    }
}

int main() {
    run_tests();
    return 0;
}
