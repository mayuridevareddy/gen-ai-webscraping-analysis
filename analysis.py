import pandas as pd

# Load dataset
df = pd.read_csv("all_books.csv")

# Clean data
df = df.dropna()

print("Dataset Info:")
print(df.info())

print("\nSummary:")
print(df.describe())

# Take sample
sample = df.head(10)

# Save sample
with open("sample_data.txt", "w") as f:
    f.write(sample.to_string())

print("\nSample saved successfully!")