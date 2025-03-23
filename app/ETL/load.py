import pandas as pd
import os

def load_dataframe_excel(df: pd.DataFrame, file_path: str = "././data/output/",file_name: str="absenteeism"):
    """
    Function to load a dataframe into a excel file.

    Args:
        data (pd.DataFrame): The dataframe to load.
        file_path (str): Path of the folder to save the file.
        file_name (str): File name.
    """
    if os.path.isdir(file_path) == False:
        os.makedirs(file_path)

    df.to_excel(str(file_path + file_name + ".xlsx"), index=False)