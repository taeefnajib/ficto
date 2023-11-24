.. Ficto documentation master file, created by
   sphinx-quickstart on Sat Nov 25 01:44:43 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Ficto - Generate Realistic Demo Data
=====================================

Ficto is a Python package that allows you to effortlessly generate realistic demo data in CSV or JSON format. With Ficto, you can create datasets with various column types by simply specifying them in a YAML configuration file.

Features
----------------------------
* Flexible Configuration: Customize your dataset by defining columns and their types in a YAML file.
* Multiple Formats: Generate datasets in either CSV or JSON format.
* Easy Installation: Install Ficto effortlessly with a single pip command.
* Realistic Demo Data: Create realistic data for testing purpose.
* Command-Line Interface (CLI): User-friendly CLI for quick and simple data generation.

Installation & Quick Start
---------------------------

To install Ficto, use the following `pip` command:


.. code-block:: bash

   pip install ficto

Generate a dataset by providing a YAML configuration file, the number of rows, and the desired file format. For example, to generate a CSV file with 100 rows using a configuration file named config.yaml, run the following command:

.. code-block:: bash

   ficto -d config.yaml -n 100 -f csv

This command generates a CSV file inside a newly created `data` folder with 100 rows of demo data based on your data configuration file (i.e.`config.yaml`).

.. toctree::
   :maxdepth: 4
   :caption: Contents:
   
   modules
   config

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
