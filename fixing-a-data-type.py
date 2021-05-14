import pandas as pd 
ri = pd.read_csv('police.csv')
print(ri.is_arrested.head())
ri['is_arrested'] = ri.is_arrested.astype('bool')
print(ri.is_arrested.dtype)
