import pandas as pd 
path = 'C:/Users/user9/Desktop/decoco/machine-readable-business-employment-data-Jun-2024-quarter.csv'
data = pd.read_csv(path)
print(data.iloc[:, :2])