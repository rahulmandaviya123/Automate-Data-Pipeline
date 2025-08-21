import os
import pandas as pd
import glob
import shutil
from datetime import datetime, timedelta

def process_files(input_folder, processed_folder, archive_folder):
    os.makedirs(processed_folder, exist_ok=True)
    os.makedirs(archive_folder, exist_ok=True)

    csv_files = glob.glob(os.path.join(input_folder, "*.csv"))
    for file in csv_files:
        df = pd.read_csv(file)
        print(f"Processing file: {os.path.basename(file)}")
        
        # Example processing step: save processed copy
        processed_file = os.path.join(processed_folder, os.path.basename(file))
        df.to_csv(processed_file, index=False)
    
    # Archive processed files older than 1 day
    cutoff_time = datetime.now() - timedelta(days=1)
    processed_files = glob.glob(os.path.join(processed_folder, "*.csv"))
    
    for file_path in processed_files:
        file_mtime = datetime.fromtimestamp(os.path.getmtime(file_path))
        if file_mtime < cutoff_time:
            archive_file = os.path.join(archive_folder, os.path.basename(file_path))
            shutil.move(file_path, archive_file)
            print(f"Archived file: {os.path.basename(file_path)}")

if __name__ == "__main__":
    process_files("data", "data/processed", "data/archive")
