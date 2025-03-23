import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pandas as pd
from unittest import mock
from app.ETL.load import load_dataframe_excel

def test_load_dataframe_excel():
    df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
    file_path = "./test_data/"
    file_name = "test_file"
    full_path = os.path.join(file_path, file_name + ".xlsx")
    
    with mock.patch("os.path.isdir", return_value=False), \
         mock.patch("os.makedirs") as mock_makedirs, \
         mock.patch("pandas.DataFrame.to_excel") as mock_to_excel:
        
        load_dataframe_excel(df, file_path, file_name)
        
        mock_makedirs.assert_called_once_with(file_path)
        mock_to_excel.assert_called_once_with(full_path, index=False)

def test_load_dataframe_excel_existing_directory():
    df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
    file_path = "./test_data/"
    file_name = "test_file"
    full_path = os.path.join(file_path, file_name + ".xlsx")
    
    with mock.patch("os.path.isdir", return_value=True), \
         mock.patch("os.makedirs") as mock_makedirs, \
         mock.patch("pandas.DataFrame.to_excel") as mock_to_excel:
        
        load_dataframe_excel(df, file_path, file_name)
        
        mock_makedirs.assert_not_called()
        mock_to_excel.assert_called_once_with(full_path, index=False)
