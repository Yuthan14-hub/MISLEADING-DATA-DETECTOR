import pandas as pd

def validate_schema(df, schema):
    """
    Validate a DataFrame against a schema.
    
    Args:
        df (pd.DataFrame): DataFrame to validate
        schema (dict): Dictionary mapping column names to expected data types
        
    Returns:
        dict: Validation results with status and details
    """
    results = {
        "valid": True,
        "errors": [],
        "warnings": []
    }
    
    # Check if all schema columns exist in DataFrame
    for col, dtype in schema.items():
        if col not in df.columns:
            results["valid"] = False
            results["errors"].append(f"Missing column: {col}")
        else:
            # Check if column type matches expected type
            expected_type = pd.api.types.pandas_dtype(dtype)
            actual_type = df[col].dtype
            
            if actual_type != expected_type:
                try:
                    # Try to convert
                    df[col] = df[col].astype(dtype)
                    results["warnings"].append(f"Column '{col}': converted from {actual_type} to {dtype}")
                except (ValueError, TypeError) as e:
                    results["valid"] = False
                    results["errors"].append(f"Column '{col}': cannot convert {actual_type} to {dtype} - {str(e)}")
    
    # Check for extra columns
    extra_cols = set(df.columns) - set(schema.keys())
    if extra_cols:
        results["warnings"].append(f"Extra columns found: {extra_cols}")
    
    results["schema"] = schema
    results["dataframe_shape"] = df.shape
    results["dataframe_columns"] = list(df.columns)
    
    return results