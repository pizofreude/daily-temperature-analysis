# Import libraries
import unittest
from daily_temperature_analysis import temperature_data

# Define a test class that inherits from unittest.TestCase:
class TestDailyTemperatureAnalysis(unittest.TestCase):
    def test_temperature_data(self):
        # Assert
        # Write an assertion to verify the expected behavior of the temperature_data variable
        self.assertIsInstance(temperature_data, list)
        self.assertGreaterEqual(len(temperature_data), 24)
        # Add more assertions as needed

