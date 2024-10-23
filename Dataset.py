import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Check if the file exists
file_path = './Dataset.csv'
if not os.path.exists(file_path):
    raise FileNotFoundError(f"The file at {file_path} does not exist.")

# Load dataset
df = pd.read_csv(file_path)

# Display basic information about the dataset
print("Basic Information:")
print(df.info())
print("\nSummary Statistics:")
print(df.describe())

# Data Cleaning
# Handling missing data (example: forward fill missing values)
df = df.fillna(method='ffill')  # Choose an appropriate method based on your dataset

# Remove duplicates
df = df.drop_duplicates()

# Data exploration
print(df.head())  # Show first few rows of the dataframe
print(df.info())  # Information about the dataframe, columns, and types
print(df.describe())  # Statistical summary of the numeric columns

# Check the column names to ensure they match expectations
print("Columns in dataset:", df.columns)

# Data visualization
plt.figure(figsize=(10, 6))
plt.plot(df['Year'], df['Population'])
plt.xlabel('Year')
plt.ylabel('Population')
plt.title('Capetown Informal Settlements Population Growth')
plt.show()

# Data Manipulation
# Example 1: Grouping by a categorical variable and finding the mean of a numerical column
grouped_df = df.groupby('category_column')['numerical_column'].mean()  # Replace as needed
print("\nGrouped Data (Mean of numerical_column by category_column):")
print(grouped_df)

# Example 2: Creating a new column by applying a calculation (replace 'existing_column' with an actual column)
df['new_column'] = df['existing_column'] * 2  # Replace as needed
print("\nData with New Column:")
print(df.head())

# Bar chart for location-wise population
location_groups = df.groupby('Location')['Population'].sum().reset_index()
plt.figure(figsize=(10, 6))
plt.bar(location_groups['Location'], location_groups['Population'])
plt.xlabel('Location')
plt.ylabel('Population')
plt.title('Location-wise Population Distribution')
plt.xticks(rotation=45)  # Rotate x-axis labels if there are many locations
plt.tight_layout()
plt.show()

# Pie chart for year-wise population
year_groups = df.groupby('Year')['Population'].sum().reset_index()
plt.figure(figsize=(10, 6))
plt.pie(year_groups['Population'], labels=year_groups['Year'], autopct='%1.1f%%')
plt.title('Year-wise Population Distribution')
plt.show()

# Data analysis
population_growth = df['Population'].sum()
print("Total population growth:", population_growth)

# Group by location
location_grouped_population = df.groupby('Location')['Population'].sum()
print(location_grouped_population)

# Filter by year
year_2024 = df[df['Year'] == 2024]
print("Data for the year 2024:\n", year_2024)

# Calculate average population per year
avg_population_per_year = df.groupby('Year')['Population'].mean()
print("Average population per year:\n", avg_population_per_year)

# Calculate total area
total_area = df['Area_Sq_Km'].sum()
print("Total area:", total_area)

# Calculate population density
population_density = df['Population'].sum() / total_area
print("Population density (people per square km):", population_density)