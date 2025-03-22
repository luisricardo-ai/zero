import pandas as pd

def concatenate_dataframes(data: list[pd.DataFrame]) -> pd.DataFrame:
    """
    Return a unique dataframe based on a list of pandas dataframes.
    
    Args:
        data (list[pd.DataFrame]): List of pandas Dataframes to concatenate.

    Return:
        pd.DataFrame: Unique dataframe with all data.
    """

    if not data:
        raise ValueError("No data concatenate.") 
    
    return pd.concat(objs=data, ignore_index=True)