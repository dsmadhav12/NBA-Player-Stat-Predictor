from kaggle.api.kaggle_api_extended import KaggleApi


# Initialize Kaggle API
api = KaggleApi()
api.authenticate()

# Download the dataset
api.dataset_download_files('owenrocchi/nba-advanced-stats-20022022', path='datasets', unzip=True)