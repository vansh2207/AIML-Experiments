import pandas as pd

def load_dataset(file_path):
   
    return pd.read_csv('C:\\Users\\DELL\\OneDrive\\Documents\\EXP2.csv')

def export_dataset(df, file_path):
   
    df.to_csv('C:\\Users\\DELL\\OneDrive\\Documents\\EXP2.csv', index=False) 
    print(f"Dataset successfully exported to {file_path}")

def dataset_details(df):
   
    print("Number of Rows:", df.shape[0])
    print("Number of Columns:", df.shape[1])
    print("\nFirst Five Rows:\n", df.head())
    print("\nDataset Size:", df.size)
    print("\nNumber of Missing Values:\n", df.isnull().sum())
    print("\nSum of Numerical Columns:\n", df.sum(numeric_only=True))
    print("\nAverage of Numerical Columns:\n", df.mean(numeric_only=True))
    print("\nMinimum Values of Numerical Columns:\n", df.min(numeric_only=True))
    print("\nMaximum Values of Numerical Columns:\n", df.max(numeric_only=True))


if __name__ == "__main__":
    
    df = load_dataset("your_dataset.csv")
  
    dataset_details(df)