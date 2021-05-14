import pandas as pd
ri = pd.read_csv('police.csv')
combined = ri.stop_date.str.cat(ri.stop_time, sep=' ')
ri['stop_datetime'] = pd.to_datetime(combined)
ri.set_index('stop_datetime', inplace=True)
print(ri.index)
print(ri.columns)