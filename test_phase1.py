import sys
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

sys.path.insert(0, os.path.abspath("."))

try:
    from src.ingestion.loader import load_csv
    from src.ingestion.schema_validator import validate_schema
    logger.info("Successfully imported modules")
except ImportError as e:
    logger.error(f"Failed to import modules: {e}")
    sys.exit(1)

try:
    # Load CSV file
    csv_path = "data/raw/sample.csv"
    logger.info(f"Loading CSV from: {csv_path}")
    df = load_csv(csv_path)
    logger.info(f"Successfully loaded {len(df)} rows")
    
    # Define schema
    schema = {
        "age": "int64",
        "gender": "object",
        "income": "float64"
    }
    logger.info("Validating schema...")
    
    # Validate schema
    result = validate_schema(df, schema)
    
    # Print results
    if result["valid"]:
        logger.info("✓ Schema validation PASSED")
    else:
        logger.error("✗ Schema validation FAILED")
        for error in result["errors"]:
            logger.error(f"  - {error}")
    
    if result["warnings"]:
        for warning in result["warnings"]:
            logger.warning(f"  - {warning}")
    
    print("\n" + "="*50)
    print("VALIDATION RESULTS")
    print("="*50)
    print(f"Valid: {result['valid']}")
    print(f"Shape: {result['dataframe_shape']}")
    print(f"Columns: {result['dataframe_columns']}")
    if result["errors"]:
        print(f"Errors: {result['errors']}")
    if result["warnings"]:
        print(f"Warnings: {result['warnings']}")
    print("="*50)
    
except FileNotFoundError as e:
    logger.error(f"File error: {e}")
    sys.exit(1)
except ValueError as e:
    logger.error(f"Validation error: {e}")
    sys.exit(1)
except Exception as e:
    logger.error(f"Unexpected error: {e}", exc_info=True)
    sys.exit(1)