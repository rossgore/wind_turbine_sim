import unittest
from wind_turbine import WindTurbine

class TestWindTurbine(unittest.TestCase):
    def setUp(self):
        self.turbine = WindTurbine(nominal_power=1.5e6, base_wind_speed=12, base_rotational_speed=1.2)

    def test_nominal_conditions(self):
        power_slow_rotation = self.turbine.calculate_power(wind_speed=12, rotational_speed=1.1, pitch_angle=0)
        self.assertLess(power_slow_rotation, 1.5e6)

    def test_low_wind_speed(self):
        power = self.turbine.calculate_power(wind_speed=6, rotational_speed=1.2, pitch_angle=0)
        self.assertLess(power, 1.5e6)

    def test_high_wind_speed(self):
        power_above_base = self.turbine.calculate_power(wind_speed=13, rotational_speed=1.2, pitch_angle=0)
        self.assertAlmostEqual(power_above_base, 1.5e6, delta=1e4)  # Should be at or near nominal power
        
    def test_pitch_angle_effect(self):
        # Original test
        power_no_pitch = self.turbine.calculate_power(wind_speed=12, rotational_speed=1.2, pitch_angle=0)
        power_with_pitch = self.turbine.calculate_power(wind_speed=12, rotational_speed=1.2, pitch_angle=10)
        self.assertGreater(power_no_pitch, power_with_pitch)

        # Additional tests
        # Test with various pitch angles
        power_small_pitch = self.turbine.calculate_power(wind_speed=12, rotational_speed=1.2, pitch_angle=5)
        power_large_pitch = self.turbine.calculate_power(wind_speed=12, rotational_speed=1.2, pitch_angle=20)
    
        self.assertGreater(power_no_pitch, power_small_pitch)
        self.assertGreater(power_small_pitch, power_with_pitch)
        self.assertGreater(power_with_pitch, power_large_pitch)

        # Test pitch effect at different wind speeds
        power_high_wind_no_pitch = self.turbine.calculate_power(wind_speed=20, rotational_speed=1.2, pitch_angle=0)
        power_high_wind_with_pitch = self.turbine.calculate_power(wind_speed=20, rotational_speed=1.2, pitch_angle=10)
    
        self.assertGreater(power_high_wind_no_pitch, power_high_wind_with_pitch)

    def test_rotational_speed_effect(self):
        # Original test
        power_nominal = self.turbine.calculate_power(wind_speed=12, rotational_speed=1.2, pitch_angle=0)
        power_low = self.turbine.calculate_power(wind_speed=12, rotational_speed=0.8, pitch_angle=0)
        power_high = self.turbine.calculate_power(wind_speed=12, rotational_speed=1.5, pitch_angle=0)
    
        self.assertGreater(power_nominal, power_low)
        self.assertLess(power_nominal, power_high)

        # Additional tests
        # Test with more rotational speeds
        power_very_low = self.turbine.calculate_power(wind_speed=12, rotational_speed=0.5, pitch_angle=0)
        power_slightly_low = self.turbine.calculate_power(wind_speed=12, rotational_speed=1.1, pitch_angle=0)
        power_slightly_high = self.turbine.calculate_power(wind_speed=12, rotational_speed=1.3, pitch_angle=0)
        power_very_high = self.turbine.calculate_power(wind_speed=12, rotational_speed=2.0, pitch_angle=0)

        self.assertLess(power_very_low, power_low)
        self.assertLess(power_low, power_slightly_low)
        self.assertLess(power_slightly_low, power_nominal)
        
        self.assertLess(power_slightly_high, power_high)
        self.assertLess(power_high, power_very_high)

        # Test rotational speed effect at different wind speeds
        power_low_wind_nominal = self.turbine.calculate_power(wind_speed=8, rotational_speed=1.2, pitch_angle=0)
        power_low_wind_low = self.turbine.calculate_power(wind_speed=8, rotational_speed=0.8, pitch_angle=0)
        power_low_wind_high = self.turbine.calculate_power(wind_speed=8, rotational_speed=1.5, pitch_angle=0)

        self.assertGreater(power_low_wind_nominal, power_low_wind_low)
        self.assertLess(power_low_wind_nominal, power_low_wind_high)

    def test_zero_wind_speed(self):
        power = self.turbine.calculate_power(wind_speed=0, rotational_speed=1.2, pitch_angle=0)
        self.assertAlmostEqual(power, 0, delta=1e-6)

    def test_negative_wind_speed(self):
        with self.assertRaises(ValueError):
            self.turbine.calculate_power(wind_speed=-5, rotational_speed=1.2, pitch_angle=0)

    def test_negative_rotational_speed(self):
        with self.assertRaises(ValueError):
            self.turbine.calculate_power(wind_speed=12, rotational_speed=-1.2, pitch_angle=0)

    def test_negative_pitch_angle(self):
        with self.assertRaises(ValueError):
            self.turbine.calculate_power(wind_speed=12, rotational_speed=1.2, pitch_angle=-10)

if __name__ == '__main__':
    unittest.main()