import io
import sqlalchemy
import pandas as pd
from data_introspection import create_introspector
from team6_package import generate_data, save_to_csv, load_schema
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data(*args, **kwargs):
    """
    This function loads a table of data from a sqlite database

    PARAMETERS:

    db_location: path to the sqlite database to load from
    table_name: name of the table inside the sqlite database to load from
    """
    db_location='/home/src/databases/example.db'
    table_name='investment_entries'

    # View the existing tables in the sqlite database
    introspector = create_introspector('sqlite', db_path=db_location)
    tables = introspector.get_table_names()
    print(f"Tables found in source database: {tables}")

    try:
        # Load a table from the database for transformation
        return pd.read_sql(table_name, f'sqlite:///{db_location}')
    except:
        # Print error message and return empty dataframe
        print("ERROR: Database or table specified could not be found")
        return pd.DataFrame()


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
