import sys
import os

sys.path.append(os.path.abspath("."))

from src.ingestion.loader import load_csv
from src.ingestion.schema_validator import validate_schema

df = load_csv("data/raw/sample.csv")

schema = {
    "age": "int64",
    "gender": "object",
    "income": "float64"
}

result = validate_schema(df, schema)
print(result)
