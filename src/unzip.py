import zipfile
import os

# Define the paths
zip_file = "data/nba-advanced-stats-20022022.zip"
extract_dir = "data/"

# Extract the ZIP file
with zipfile.ZipFile(zip_file, 'r') as zip_ref:
    zip_ref.extractall(extract_dir)

# Verify extraction
print("Extracted files:")
print(os.listdir(extract_dir))