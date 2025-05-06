import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Task 1: Load and Explore the Dataset
# Load the dataset
df = pd.read_csv("XAUUSDm_H4.csv")

# Display the first few rows
print("First 5 rows of the dataset:")
print(df.head())

# Explore the structure of the dataset
print("\nDataset Info:")
print(df.info())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Clean the dataset (drop rows with missing values)
df_clean = df.dropna()
print(f"\nCleaned dataset has {df_clean.shape[0]} rows and {df_clean.shape[1]} columns.")

# Task 2: Basic Data Analysis

# Basic statistics for numerical columns
print("\nBasic Statistics:")
print(df_clean.describe())

# Group by time and calculate OHLC mean for each period (for example, by every 4 hours)
df_clean['time'] = pd.to_datetime(df_clean['time'])
df_clean.set_index('time', inplace=True)

# Group by day or month (you can change the frequency based on your needs)
ohlc_data = df_clean.resample('D').agg({'open': 'first', 'high': 'max', 'low': 'min', 'close': 'last'})
print("\nAggregated OHLC data (daily):")
print(ohlc_data.head())

# Task 3: Data Visualization

# Line Chart: Plot close price over time
plt.figure(figsize=(10, 5))
plt.plot(df_clean.index, df_clean['close'], marker='o', color='blue')
plt.title("Close Price Over Time")
plt.xlabel("Date")
plt.ylabel("Close Price")
plt.grid(True)
plt.tight_layout()
plt.show()

# Bar Chart: Plot daily high vs low range (High-Low) 
daily_range = ohlc_data['high'] - ohlc_data['low']
plt.figure(figsize=(6, 4))
daily_range.plot(kind='bar', color='orange')
plt.title("Daily High-Low Range")
plt.xlabel("Date")
plt.ylabel("Range (High - Low)")
plt.tight_layout()
plt.show()

# Histogram: Distribution of closing prices
plt.figure(figsize=(6, 4))
plt.hist(df_clean['close'], bins=50, edgecolor='black', color='skyblue')
plt.title("Close Price Distribution")
plt.xlabel("Close Price")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# Scatter Plot: Relationship between 'high' and 'low' prices
plt.figure(figsize=(6, 4))
sns.scatterplot(x=df_clean['high'], y=df_clean['low'], color='green')
plt.title("High vs Low Prices")
plt.xlabel("High Price")
plt.ylabel("Low Price")
plt.tight_layout()
plt.show()
