def validate_schema(df, expected_schema: dict):
    """
    expected_schema example:
    {
        "age": "int64",
        "gender": "object",
        "income": "float64"
    }
    """
    errors = []

    for column, dtype in expected_schema.items():
        if column not in df.columns:
            errors.append(f"Missing column: {column}")
        else:
            if df[column].dtype.name != dtype:
                errors.append(
                    f"Type mismatch in '{column}': expected {dtype}, got {df[column].dtype.name}"
                )

    return {
        "is_valid": len(errors) == 0,
        "errors": errors
    }
