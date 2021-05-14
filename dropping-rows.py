import pandas as pd
ri = pd.read_csv('police.csv')
print(ri.isnull().sum())
ri.dropna(subset=['driver_gender'], inplace=True)
print(ri.isnull().sum())
print(ri.shape)