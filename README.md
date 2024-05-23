# Deforestation, Climate Change, and Economic Impacts

This project analyzes the impacts of deforestation and climate change, including economic factors. The analysis includes data visualization, correlation analysis, and forecasting.

## Project Structure

- `deforestation_analysis.py`: Script for initial data loading, cleaning, and visualization.
- `correlation_analysis.py`: Script for analyzing correlations between different datasets.
- `forecasting_analysis.py`: Script for forecasting future trends based on historical data.
- `requirements.txt`: List of Python packages required to run the scripts.
- `README.md`: Project documentation.
- `analysis_summary.md`: Overall summary of the analysis, including interpretations of the graphs, correlation matrix, and forecasted data.

## Setup

1. **Create a virtual environment**:
    ```bash
    python -m venv venv
    ```

2. **Activate the virtual environment**:
    - On Windows:
      ```bash
      venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

3. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the scripts**:
    ```bash
    python deforestation_analysis.py
    python correlation_analysis.py
    python forecasting_analysis.py
    ```

## Data Sources

- **Climate Data**: National Centers for Environmental Information (NCEI)
- **Deforestation Data**: Global Forest Watch
- **Economic Data**: World Bank

## Data Files

- `climate_data.csv`: Contains data on temperature changes with respect to a baseline climatology.
- `treecoverloss_data.csv`: Contains data on tree cover loss over the years.
- `economic_data.csv`: Contains data on employment in agriculture as a percentage of male employment.
- `combined_data.csv`: Merged dataset combining climate data, deforestation data, and economic data.

## Scripts

### `deforestation_analysis.py`

This script loads the climate, deforestation, and economic data, merges them into a single dataset, and visualizes the trends.

### `correlation_analysis.py`

This script loads the combined dataset and performs a correlation analysis between temperature change, tree cover loss, and agricultural employment.

### `forecasting_analysis.py`

This script uses linear regression to forecast future trends in tree cover loss based on historical data.

## Usage

Run each script in the specified order to perform the full analysis. Ensure that all the CSV files are placed in the `data/` directory.

1. **Run the deforestation analysis**:
    ```bash
    python deforestation_analysis.py
    ```

2. **Run the correlation analysis**:
    ```bash
    python correlation_analysis.py
    ```

3. **Run the forecasting analysis**:
    ```bash
    python forecasting_analysis.py
    ```

## Requirements

The project requires the following Python packages:
- pandas
- matplotlib
- scikit-learn
- numpy

Install these packages using `pip`:
```bash
pip install -r requirements.txt

## Data Sources

- **Temperature Change Data**: International Monetary Fund
- **Tree Cover Loss**: Global Forest Watch
- **Economic Data**: World Bank

## Interactive Dashboard

You can view the interactive Tableau dashboard [here](https://public.tableau.com/views/AnalysisofClimateChangeDeforestationandEconomicImpacts/Dashboard1?:language=en-US&publish=yes&:sid=&:display_count=n&:origin=viz_share_link).

