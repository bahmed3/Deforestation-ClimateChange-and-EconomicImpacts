import pandas as pd
import matplotlib.pyplot as plt

# Load the climate data
climate_data_path = r'C:\Users\notbi\OneDrive\Documents\deforestation\data\temp_change.csv'
climate_data = pd.read_csv(climate_data_path)
climate_data['Year'] = climate_data['Year'].astype(int)
print("Climate Data Columns:", climate_data.columns)

# Load the deforestation (tree cover loss) data
deforestation_data_path = r'C:\Users\notbi\OneDrive\Documents\deforestation\data\treecoverloss.csv'
deforestation_data = pd.read_csv(deforestation_data_path)
deforestation_data = deforestation_data[['Year', 'Tree Cover Loss (ha)']]  # Select relevant columns
deforestation_data['Year'] = deforestation_data['Year'].astype(int)

# Load the economic data
economic_data_path = r'C:\Users\notbi\OneDrive\Documents\deforestation\data\economic_data.csv'
economic_data = pd.read_csv(economic_data_path)
economic_data['Year'] = economic_data['Year'].astype(int)

# Merge datasets
combined_data = pd.merge(climate_data[['Year', 'Temperature change with respect to a baseline climatology, corresponding to the period 1951-1980']], deforestation_data, on='Year', how='inner')
combined_data = pd.merge(combined_data, economic_data, on='Year', how='inner')

print(combined_data.head())
print("Combined Data Columns:", combined_data.columns)

temperature_column = 'Temperature change with respect to a baseline climatology, corresponding to the period 1951-1980'
employment_column = 'Employment in agriculture, male (% of male employment)'

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 18), sharex=True)

# Temperature Change Plot
ax1.plot(combined_data['Year'], combined_data[temperature_column], color='red', marker='o', linestyle='-', label='Temperature Change (°C)')
ax1.set_ylabel('Temperature Change (°C)', color='red')
ax1.tick_params(axis='y', labelcolor='red')
ax1.legend(loc='upper left')
ax1.set_title('Temperature Change, Tree Cover Loss, and Agricultural Employment Over Time')

# Tree Cover Loss Plot
ax2.plot(combined_data['Year'], combined_data['Tree Cover Loss (ha)'], color='blue', marker='x', linestyle='-', label='Tree Cover Loss (ha)')
ax2.set_ylabel('Tree Cover Loss (ha)', color='blue')
ax2.tick_params(axis='y', labelcolor='blue')
ax2.legend(loc='upper left')

# Agricultural Employment Plot
ax3.plot(combined_data['Year'], combined_data[employment_column], color='green', marker='s', linestyle='-', label='Agricultural Employment (%)')
ax3.set_xlabel('Year')
ax3.set_ylabel('Agricultural Employment (%)', color='green')
ax3.tick_params(axis='y', labelcolor='green')
ax3.legend(loc='upper left')

plt.show()

combined_data_path = 'data/combined_data.csv'
combined_data.to_csv(combined_data_path, index=False)