import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder

file_path = "data/active_players.csv"
data = pd.read_csv(file_path)
#formats data set to be used in model
data = data.drop(columns=['year'])
label_encoder = LabelEncoder()
data['Pos'] = label_encoder.fit_transform(data['Pos'])

# gets rid of PER to prevent model from being trained on actual values
X = data.drop(columns=['PER', 'Player']) 
Y = data['PER']
X = X.apply(pd.to_numeric, errors='coerce')


# Split the data into training and testing sets
X_train, X_test, Y_train, Y_test, player_names_train, player_names_test = train_test_split(
    X, Y, data['Player'], test_size=0.2, random_state=42)

# Initialize and fits the model
model = RandomForestRegressor()
model.fit(X_train, Y_train)

# Make predictions
Y_prediction = model.predict(X_test)

# Create a DataFrame so outputfile can easily be viewed
output_data = pd.DataFrame({
    'Player': player_names_test,
    'Actual PER': Y_test,
    'Predicted PER': Y_prediction,
    'Difference': Y_prediction - Y_test
})

#finds the average difference
differences_array = output_data['Difference'].to_numpy()
average_difference = np.mean(differences_array)

output_data = output_data.drop_duplicates(subset='Player')
output_data = output_data.sort_values(by='Player')

# write to csvfile
output_file_path = "output/predicted_performance.csv"
output_data.to_csv(output_file_path, index=False)

print("Average difference in PER: "+ str(average_difference))
