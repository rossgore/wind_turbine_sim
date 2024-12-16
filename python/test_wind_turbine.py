import numpy as np
from wind_turbine import calculate_power_output

# Test cases
Vw_values = [5, 7, 8, 10, 12, 14]
ww_pu_values = np.arange(0, 3.05, 0.05)  # Include 3 in the range

def run_tests():
    for Vw in Vw_values:
        print(f"\nWind Speed (Vw): {Vw} m/s")
        print("Generator Speed (ww_pu) | Power Output (Pmw_pu)")
        print("-" * 45)
        for ww_pu in ww_pu_values:
            Pmw_pu = calculate_power_output(Vw, ww_pu)
            print(f"{ww_pu:.2f} | {Pmw_pu:.4f}")

if __name__ == "__main__":
    run_tests()