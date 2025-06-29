import pandas as pd

# Load Excel file
file_path = r'Online_Retail_Data_Set.xlsx'  #Original File Path
df = pd.read_excel(file_path)

# Remove rows where Quantity is less than 1
df = df[df['Quantity'] >= 1]

# Remove rows where UnitPrice is less than 0
df = df[df['UnitPrice'] >= 0]

# Optionally drop rows with missing CustomerID (if needed for Q3)
df = df.dropna(subset=['CustomerID'])

# Save the cleaned dataset
cleaned_path = r'Online_Retail_Cleaned.xlsx' # Cleaned File Path
df.to_excel(cleaned_path, index=False)

print(f"Cleaned data saved to: {cleaned_path}")
