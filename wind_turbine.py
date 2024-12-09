import numpy as np

class WindTurbine:
    def __init__(self, nominal_power, base_wind_speed, base_rotational_speed):
        self.nominal_power = nominal_power  # W
        self.base_wind_speed = base_wind_speed  # m/s
        self.base_rotational_speed = base_rotational_speed  # pu
        
        # Coefficients for Cp calculation
        self.c1 = 0.5176
        self.c2 = 116
        self.c3 = 0.4
        self.c4 = 5
        self.c5 = 21
        self.c6 = 0.0068
        
        # Calculate rotor radius based on nominal power and Betz limit
        self.rotor_radius = np.sqrt((2 * nominal_power) / (1.225 * np.pi * 0.48 * base_wind_speed**3))
        
        # Calculate power gain kp
        self.kp = 0.73  # As specified in the PDF

    def calculate_power(self, wind_speed, rotational_speed, pitch_angle):
        if wind_speed < 0 or rotational_speed < 0 or pitch_angle < 0:
            raise ValueError("Wind speed, rotational speed, and pitch angle must be non-negative")
        
        if wind_speed == 0:
            return 0  # No power output for zero wind speed
        
        # Calculate tip speed ratio and Cp
        tip_speed_ratio = self.tip_speed_ratio(wind_speed, rotational_speed)
        cp = self.calculate_cp(tip_speed_ratio, pitch_angle)
        
        # Calculate power in per-unit
        wind_speed_pu = wind_speed / self.base_wind_speed
        power_pu = self.kp * cp * wind_speed_pu**3
        
        # Convert power from per-unit to watts
        power = power_pu * self.nominal_power
        
        # Cap the power output at the nominal power
        return min(power, self.nominal_power)

    def tip_speed_ratio(self, wind_speed, rotational_speed):
        if wind_speed == 0:
            return float('inf')
        return (rotational_speed * self.base_rotational_speed * self.rotor_radius * 2 * np.pi) / (wind_speed * 60)
        
    def calculate_cp(self, lambda_tsr, pitch_angle):
        lambda_i = 1 / (1 / (lambda_tsr + 0.08 * pitch_angle) - 0.035 / (pitch_angle**3 + 1))
        cp = self.c1 * (self.c2 / lambda_i - self.c3 * pitch_angle - self.c4) * np.exp(-self.c5 / lambda_i) + self.c6 * lambda_tsr
        return max(0, min(cp, 16/27))