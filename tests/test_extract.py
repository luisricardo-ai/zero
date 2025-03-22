import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from unittest.mock import patch
import pandas as pd
from app.ETL.extract import extract_excel # Replace with the actual module name

test_df = pd.DataFrame({"col1": [1, 2], "col2": [3, 4]})

@patch("app.ETL.extract.glob.glob")
@patch("app.ETL.extract.pd.read_excel")
def test_extract_excel_success(mock_read_excel, mock_glob):
    # Mock the files returned by glob
    mock_glob.return_value = ["file1.xlsx", "file2.xlsx"]
    
    # Mock read_excel to return a test DataFrame
    mock_read_excel.side_effect = [test_df, test_df]
    
    result = extract_excel("data/input/")
    
    assert len(result) == 2
    assert all(isinstance(df, pd.DataFrame) for df in result)

@patch("app.ETL.extract.glob.glob")
def test_extract_excel_no_files(mock_glob):
    # Mock an empty file list
    mock_glob.return_value = []
    
    with pytest.raises(ValueError, match="No Excel files found in the specified folder"):
        extract_excel("data/input/")
