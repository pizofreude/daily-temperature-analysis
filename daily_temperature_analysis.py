# -*- coding: utf-8 -*-
# @Author: Pizofreude
# @Date:   2023-08-08 00:00:00
# Import libraries
import os
import random
import pandas as pd
import matplotlib.pyplot as plt

# Generate random temperature data for a day
# 24 hours
# 20 - 35 °C
# 24 rows
# 8 columns
# Will be replaced with actual data from Temperature API like Open-Meteo API (FOSS)
temperature_data = [random.randint(20, 35) for _ in range(24)]

# Create a DataFrame
df = pd.DataFrame({'Hour': list(range(1, 25)), 'Temperature': temperature_data})

# Create a temperature plot
plt.plot(df['Hour'], df['Temperature'])
plt.xlabel('Hour')
plt.ylabel('Temperature (°C)')
plt.title('Daily Temperature Analysis')

# Create the directory if it doesn't exist
os.makedirs('src/plot', exist_ok=True)

# Save the plot image in the new directory
plt.savefig('src/plot/temperature_plot.png')

# Deactivate the virtual environment
os.system('deactivate')

# Commit and push changes to GitHub
os.system('git add temperature_plot.png')
os.system('git commit -m "Update temperature plot"')
os.system('git push origin main')

