import pandas as pd
import glob
import os

def load_data(data_folder: str):
    """
    Load and concatenate all CSV files in the data folder.
    """
    file_paths = glob.glob(os.path.join(data_folder, "*.csv"))
    dataframes = []
    
    for file_path in file_paths:
        df = pd.read_csv(file_path)
        dataframes.append(df)
    
    concatenated_df = pd.concat(dataframes, ignore_index=True)
    return concatenated_df
