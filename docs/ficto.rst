ficto package
=============

Subpackages
-----------

.. toctree::
   :maxdepth: 4

   ficto.core
   ficto.helper

ficto.main module
-----------------

This script provides a command-line interface for generating synthetic data files based on a specified data configuration.
It utilizes the `ficto.core.generate` module to create a DataFrame and saves it to either a CSV or JSON file.

Usage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Run the script from the command line with the required arguments
.. code-block:: bash

   python main.py -d config.yaml -n 100 -f csv

2. Customize the command-line arguments based on your data generation requirements

Arguments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* `-d`, `--dataconfig`: Path to the YAML file for data configuration.
* `-n`, `--numrows`: Number of rows.
* `-f`, `--filetype`: Type of file to be generated (csv or json).

Note
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* The script uses the `create_dataframe` function from `ficto.core.generate` to generate synthetic data.
* The generated file is saved in the 'data' sub-folder with a filename indicating the shape of the DataFrame, the number of rows, and the current timestamp.
* Supported file types are CSV and JSON.

Data Config file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This YAML file serves as a template for configuring data generation in the `ficto` package. It defines various columns,
each specifying a unique aspect of synthetic data to be generated. The configuration options include data types,
constraints, and customization parameters for different types of data.

Example:

.. code-block:: yaml
   
   columns:
      - name: ID
      type: customseq
      datatype: int
      start: 1
      step: 1
      pos: 1
      - name: First Name
      type: firstname
      datatype: string
      pos: 2
      - name: Last Name
      type: lastname
      datatype: string
      pos: 3


Column Types
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* customseq: Generates a custom sequence of integers.
* firstname: Generates first names.
* lastname: Generates last names.
* gender: Generates gender values.
* country: Generates country names.
* phonenumber: Generates phone numbers.
* currency: Generates currency codes.
* customdate: Generates custom date values.
* customint: Generates custom integer values.
* customfloat: Generates custom float values.
* customlist: Generates values from a custom list.
* customuuid: Generates custom UUID values.
* customlorem: Generates custom Lorem Ipsum text.
* email: Generates email addresses.
* website: Generates website URLs.
* organization: Generates company names.
* department: Generates department names.
* designation: Generates job designations.
* passport: Generates passport numbers.
* ssn: Generates social security numbers.
* ccn: Generates credit card numbers.
* password: Generates passwords.
* address: Generates addresses.
* lat: Generates latitude values.
* long: Generates longitude values.
* industry: Generates industry names.
* customtime: Generates custom time values.
* customyear: Generates custom year values.
* custommonth: Generates custom month values.
* prodname: Generates product names.
* prodcat: Generates product categories.


Functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. automodule:: ficto.main
   :members:
   :undoc-members:
   :show-inheritance:

.. Module contents
.. ---------------

.. .. automodule:: ficto
..    :members:
..    :undoc-members:
..    :show-inheritance:
