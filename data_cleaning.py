import pandas as pd

# Raw CSV file ka path
raw_data_path = 'data/raw_data.csv'  # Update the file path if needed

# Data ko load karna
df = pd.read_csv(raw_data_path)

# 1. Duplicate rows ko drop karna
df.drop_duplicates(inplace=True)

# 2. Missing values (NaN) ko handle karna
df['Age'].fillna(df['Age'].mean(), inplace=True)

# 3. Columns ko drop ya rename karna (agar required ho)
df.drop(columns=['UnwantedColumn'], inplace=True)

# 4. Cleaned data ko nayi CSV file mein save karna
df.to_csv('cleaned_data.csv', index=False)

print("Data cleaned successfully and saved as 'cleaned_data.csv'.")
