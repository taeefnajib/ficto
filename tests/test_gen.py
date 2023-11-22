import pytest
import pandas
from ficto.core.generate import *


good_parameters = [
    ("config-template.yaml", 100, pandas.DataFrame),
    ("config-template.yaml", 1, pandas.DataFrame),
]

@pytest.mark.parametrize("dataconfig, numrows, response", good_parameters)
def test_create_dataframe(dataconfig, numrows, response):
    assert type(create_dataframe(dataconfig, numrows)) == response
