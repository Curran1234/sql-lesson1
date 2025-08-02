import pandas as pd
import sqlite3
import os
import requests
import zipfile
from io import BytesIO
import shutil

# URL and filename of the USDA Food Data Central CSV dataset
url = "https://fdc.nal.usda.gov/fdc-datasets/FoodData_Central_csv_2024-04-18.zip"
zip_filename = "FoodData_Central_csv_2024-04-18.zip"
data_folder = './data/'
db_filename = 'usda_food_data.db'

def ensure_data_folder():
    if not os.path.exists(data_folder):
        os.makedirs(data_folder)

def download_file(url, save_path):
    print(f"Downloading {url}...")
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print("Download complete.")
    else:
        raise Exception(f"Failed to download the file. Status code: {response.status_code}")

def extract_zip(zip_path, extract_to):
    print(f"Extracting {zip_path}...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    
    # Move CSV files from potential subfolder to main data folder
    extracted_folder = next(os.walk(extract_to))[1][0]  # Get the first subfolder
    extracted_path = os.path.join(extract_to, extracted_folder)
    for file in os.listdir(extracted_path):
        if file.endswith('.csv'):
            shutil.move(os.path.join(extracted_path, file), extract_to)
    
    # Remove the now-empty subfolder
    shutil.rmtree(extracted_path)
    print("Extraction complete and files moved to data folder.")

def import_csv_to_sqlite(db_path):
    conn = sqlite3.connect(db_path)
    csv_files = [f for f in os.listdir(data_folder) if f.endswith('.csv')]
    
    for csv_file in csv_files:
        print(f"Importing {csv_file}...")
        df = pd.read_csv(os.path.join(data_folder, csv_file))
        table_name = os.path.splitext(csv_file)[0]
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        print(f"Imported {csv_file} to table {table_name}")
    
    conn.close()

def main():
    ensure_data_folder()
    zip_path = os.path.join(data_folder, zip_filename)
    db_path = os.path.join(data_folder, db_filename)
    
    if os.path.exists(zip_path):
        print(f"ZIP file {zip_filename} already exists in the data folder.")
        if os.path.exists(db_path):
            print("Database file already exists. Assuming data is already imported.")
            return
        else:
            print("Database file not found. Proceeding with extraction and import.")
    else:
        download_file(url, zip_path)
        
    extract_zip(zip_path, data_folder)
    import_csv_to_sqlite(db_path)
    
    print("All CSV files have been imported to SQLite database.")

if __name__ == "__main__":
    main()