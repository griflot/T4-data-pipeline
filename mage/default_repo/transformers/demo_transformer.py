from kpi_formula.advanced.kpi_calculator import KPICalculator
from pandas import DataFrame
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data: DataFrame, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """

    ROIs = []
    for index, row in data.iterrows():
        # Calculate return on investment (ROI) for each entry
        ROI = KPICalculator.roi(revenue=int(row['revenue']), investment=int(row['initial_investment']))
        ROIs.append(ROI)

    # Add ROI as column in DataFrame
    data['roi'] = ROIs

    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
