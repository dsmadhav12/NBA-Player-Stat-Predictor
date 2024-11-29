import pandas as pd

datasetPath = "data/NBA_Advanced_Stats_2002-2022.csv" 
df = pd.read_csv(datasetPath)

df['Player'] = df['year-name'].str.split('-').str[1] 

df_sorted = df.sort_values(by=['Player', 'year'])

sorted_dataset_path = "data/Sorted_Stats.csv"
df_sorted.to_csv(sorted_dataset_path, index=False)
