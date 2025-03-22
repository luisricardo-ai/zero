import os
import glob
import pandas as pd

def extract_excel(input_folder: str) -> list[pd.DataFrame]:
    """
    Function to read and return the data as a list of pandas Dataframes.

    Args:
        input_folder (str): The folder name where the files are located.

    Return:
        list[pd.DataFrame]: A list of pd.DataFrame based on the excel data.
    """
    files = glob.glob(os.path.join(input_folder, "*.xlsx"))

    if not files:
        raise ValueError("No Excel files found in the specified folder")
    
    return [pd.read_excel(file) for file in files]