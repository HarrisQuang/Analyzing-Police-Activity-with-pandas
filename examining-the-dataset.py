import pandas as pd 
ri = pd.read_csv('police.csv')
print(ri.head())
print(ri.isnull().sum())