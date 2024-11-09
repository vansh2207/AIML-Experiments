import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r'C:\Users\DELL\Downloads\archive\StudentPerformanceFactors.csv')

print("Dataset Information:")
df.info()

print("\nFirst five rows of the dataset:")
print(df.head())

print("\nNumber of rows and columns:", df.shape)

print("\nSize of the dataset (total elements):", df.size)

print("\nNumber of missing values in each column:")
print(df.isnull().sum())

print("\nStatistical Summary (Numerical Columns):")
print(df.describe())

print("\nSum of numerical columns:")
print(df.sum(numeric_only=True))

print("\nAverage (mean) of numerical columns:")
print(df.mean(numeric_only=True))

print("\nMinimum values of numerical columns:")
print(df.min(numeric_only=True))

print("\nMaximum values of numerical columns:")
print(df.max(numeric_only=True))

numerical_df = df.select_dtypes(include=['float64', 'int64'])

print("\nCorrelation between numerical columns:")
print(numerical_df.corr())

plt.figure(figsize=(10, 5))
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.title('Missing Values Heatmap')
plt.show()

sns.pairplot(numerical_df)
plt.title('Pairplot of Numerical Data')
plt.show()

plt.figure(figsize=(10, 6))
sns.heatmap(numerical_df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap')
plt.show()
