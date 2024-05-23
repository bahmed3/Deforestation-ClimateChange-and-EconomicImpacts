import pandas as pd
import matplotlib.pyplot as plt

combined_data_path = r'C:\Users\notbi\OneDrive\Documents\deforestation\data\combined_data.csv'
combined_data = pd.read_csv(combined_data_path)

print("Combined Data Columns:", combined_data.columns)
print(combined_data.head())

# Perform correlation analysis
correlation_matrix = combined_data[['Temperature change with respect to a baseline climatology, corresponding to the period 1951-1980', 'Tree Cover Loss (ha)', 'Employment in agriculture, male (% of male employment)']].corr()

print("Correlation Matrix:")
print(correlation_matrix)

# Plot correlation matrix
fig, ax = plt.subplots(figsize=(10, 8))
cax = ax.matshow(correlation_matrix, cmap='coolwarm')
fig.colorbar(cax)
ticks = range(len(correlation_matrix.columns))
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xticklabels(correlation_matrix.columns, rotation=90)
ax.set_yticklabels(correlation_matrix.columns)

plt.show()
