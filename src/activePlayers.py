import pandas as pd
file_path = "data/Sorted_Stats.csv"
dataset = pd.read_csv(file_path)

dataset.drop(columns=['Unnamed: 0'], inplace=True)
dataset['year'] = pd.to_numeric(dataset['year'], errors='coerce')
dataset['Age'] = pd.to_numeric(dataset['Age'], errors='coerce')

#active cutoff
activePlayers = dataset[dataset['year'] == 2022]["Player"].unique()
newData = dataset[dataset['Player'].isin(activePlayers)]

sorted_file_path = "data/active_players.csv"
newData.to_csv(sorted_file_path, index=False)
