import kagglehub

# Download latest version
path = kagglehub.dataset_download("owenrocchi/nba-advanced-stats-20022022")

print("Path to dataset files:", path)