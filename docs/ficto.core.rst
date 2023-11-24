ficto.core package
==================

Submodules
----------

ficto.core.generate module
--------------------------

This module provides functions to create synthetic data using a YAML configuration file.
It leverages the functionality from the `ficto.helper.data_module` for data sources and
`ficto.helper.builder` for generating data based on the specified configuration.

Usage
~~~~~~~~~~~~~~~~~~~~~
1. Use the `create_dataframe` function to generate synthetic data:

.. code-block:: python

   data_config_path = "path/to/your/config.yaml"
   num_rows = 1000  # Specify the number of rows needed in the DataFrame
   synthetic_data = create_dataframe(data_config_path, num_rows)

2. Customize the YAML configuration file according to your data generation requirements.

Notes:

* The `create_dataframe` function reads the configuration from a YAML file and generates synthetic data based on the specified column types and options.
* The module utilizes functions from `ficto.helper.data_module` and `ficto.helper.builder` to source data and generate synthetic values, respectively.

Functions
~~~~~~~~~~~~~~~~~~~~~
* `create_dataframe`: Creates a pandas DataFrame based on the configuration specified in a YAML file.

.. automodule:: ficto.core.generate
   :members:
   :undoc-members:
   :show-inheritance:

Module contents
---------------

.. automodule:: ficto.core
   :members:
   :undoc-members:
   :show-inheritance:
