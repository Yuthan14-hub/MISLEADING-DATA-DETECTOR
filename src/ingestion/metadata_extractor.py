def extract_metadata(df):
    metadata = {
        "num_rows": df.shape[0],
        "num_columns": df.shape[1],
        "features": {}
    }

    for col in df.columns:
        metadata["features"][col] = {
            "dtype": df[col].dtype.name,
            "missing_values": int(df[col].isnull().sum()),
            "unique_values": int(df[col].nunique())
        }

    return metadata
