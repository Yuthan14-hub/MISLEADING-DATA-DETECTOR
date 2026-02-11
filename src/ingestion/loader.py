import pandas as pd
import os

def load_csv(filepath):
    """
    Load a CSV file into a pandas DataFrame.
    
    Args:
        filepath (str): Path to the CSV file
        
    Returns:
        pd.DataFrame: Loaded data
        
    Raises:
        FileNotFoundError: If the file doesn't exist
        ValueError: If the file is empty or invalid
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"CSV file not found: {filepath}")
    
    try:
        df = pd.read_csv(filepath)
        if df.empty:
            raise ValueError(f"CSV file is empty: {filepath}")
        return df
    except pd.errors.ParserError as e:
        raise ValueError(f"Error parsing CSV file: {e}")