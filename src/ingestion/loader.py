import pandas as pd
from sqlalchemy import create_engine

def load_csv(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    return df


def load_sql(connection_url: str, table_name: str) -> pd.DataFrame:
    engine = create_engine(connection_url)
    query = f"SELECT * FROM {table_name}"
    df = pd.read_sql(query, engine)
    return df
