import sqlalchemy
import pandas as pd
from data_introspection import create_introspector
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data(*args, **kwargs):
    """
    Template code for loading data from any source.

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """

    # View the existing tables in the sqlite database
    introspector = create_introspector('sqlite', db_path="/home/src/databases/example.db")
    tables = introspector.get_table_names()
    print(f"Tables found in source database: {tables}")

    # Load a table from the database for transformation
    return pd.read_sql('investment_entries', 'sqlite:////home/src/databases/example.db')


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
