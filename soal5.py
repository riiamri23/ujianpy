import pandas as pd

# Load the data from CSV files (assuming the files are named 'data1.csv' and 'data2.csv')
# Replace 'data1.csv' and 'data2.csv' with the actual file paths or URLs
data1 = pd.read_csv('Behavioral_Risk_Factor_Data__Tobacco_Use__2011_to_present_1.csv')
data2 = pd.read_csv('Behavioral_Risk_Factor_Data__Tobacco_Use__2011_to_present_2.csv')

# a. Check dimensions of the data
print("Dimensions of data1:", data1.shape)
print("Dimensions of data2:", data2.shape)

# b. Display the first 10 and last 10 rows of the data
print("\nFirst 10 rows of data1:")
print(data1.head(10))

print("\nLast 10 rows of data1:")
print(data1.tail(10))

print("\nFirst 10 rows of data2:")
print(data2.head(10))

print("\nLast 10 rows of data2:")
print(data2.tail(10))

# c. Merge the two dataframes based on 'LocationAbbr'
merged_data = pd.merge(data1, data2, on='LocationAbbr')

# Display the merged data
print("\nMerged Data:")
print(merged_data)

# Optionally, save the merged data to a CSV file
merged_data.to_csv('merged_data.csv', index=False)
print("\nMerged data has been saved to 'merged_data.csv'")