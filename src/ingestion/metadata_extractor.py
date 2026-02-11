def extract_metadata(df):
    """
    Extracts dataset metadata.
    """

    metadata = {
        "num_rows": df.shape[0],
        "num_columns": df.shape[1],
        "columns": list(df.columns),
        "data_types": df.dtypes.astype(str).to_dict()
    }

    return metadata
