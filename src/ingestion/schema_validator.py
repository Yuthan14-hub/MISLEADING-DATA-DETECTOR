def validate_schema(df, expected_columns=None):
    """
    Validates dataset structure.
    """

    if df is None:
        return False

    print("🔍 Validating schema...")

    # Check empty dataset
    if df.empty:
        print("❌ Dataset is empty")
        return False

    # Check expected columns (optional)
    if expected_columns:
        missing_cols = set(expected_columns) - set(df.columns)
        if missing_cols:
            print("❌ Missing columns:", missing_cols)
            return False

    print("✅ Schema validation passed")
    return True
