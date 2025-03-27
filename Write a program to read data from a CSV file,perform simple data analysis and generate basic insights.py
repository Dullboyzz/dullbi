import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the CSV file
file_path = "customers.csv"  # Update with the correct path if needed
data = pd.read_csv(file_path)

# Step 2: Display first few rows
print("\n📌 First 5 Rows of the Dataset:")
print(data.head())

# Step 3: Display basic dataset information
print("\n📌 Dataset Info:")
print(data.info())

# Step 4: Check for missing values
print("\n📌 Missing Values:")
print(data.isnull().sum())

# Step 5: Basic statistics
print("\n📌 Basic Statistics:")
print(data.describe())

# Step 6: Data Visualization
plt.figure(figsize=(12, 5))

# Histogram for Age Distribution
plt.subplot(1, 2, 1)
sns.histplot(data["Age"], bins=15, kde=True, color="blue")
plt.title("Age Distribution")

# Scatter plot for Annual Income vs. Spending Score
plt.subplot(1, 2, 2)
sns.scatterplot(x=data["Annual Income(k$)"], y=data["Spending Score(1-100)"], hue=data["Genre"])
plt.title("Annual Income vs Spending Score")

plt.tight_layout()
plt.show()

# Step 7: Insights
print("\n📌 Insights from Data Analysis:")
print(f"- The dataset contains {len(data)} customers.")
print(f"- The average annual income is ${data['Annual Income(k$)'].mean():.2f}k.")
print(f"- The average spending score is {data['Spending Score(1-100)'].mean():.2f}.")

