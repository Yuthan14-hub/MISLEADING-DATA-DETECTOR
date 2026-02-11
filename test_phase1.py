import sys
import os

# Ensure src is accessible
sys.path.insert(0, os.path.abspath("."))

from src.ingestion.loader import load_csv
from src.ingestion.schema_validator import validate_schema
from src.ingestion.metadata import extract_metadata

print("🚀 Phase 1 Started")

df = load_csv("data/raw/sample.csv")

if validate_schema(df):
    meta = extract_metadata(df)
    print("\n📊 Metadata:")
    print(meta)
