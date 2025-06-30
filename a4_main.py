import pandas as pd

# Load the dataset
df = pd.read_csv("athlete_events.csv")

# Count missing values in each column
print(df.isnull().sum())
print(f'df shape: {df.shape}')
# Drop rows missing both height and weight
df_cleaned = df.dropna(subset=['Height', 'Weight'])
print(f'cleaned df shape: {df_cleaned.shape}')