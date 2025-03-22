import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
import pandas as pd
from app.ETL.transform import concatenate_dataframes

def test_concatenate_dataframes_success():
    df1 = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
    df2 = pd.DataFrame({"A": [5, 6], "B": [7, 8]})
    
    result = concatenate_dataframes([df1, df2])
    
    assert isinstance(result, pd.DataFrame)
    assert len(result) == 4
    assert list(result.columns) == ["A", "B"]

def test_concatenate_dataframes_empty_list():
    with pytest.raises(ValueError, match="No data concatenate."):
        concatenate_dataframes([])