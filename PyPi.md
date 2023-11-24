# Ficto - Generate Realistic Demo Data

Ficto is a Python package that allows you to effortlessly generate realistic demo data in CSV or JSON format. With Ficto, you can create datasets with various column types by simply specifying them in a YAML configuration file.

## Installation & Quick Start

To install Ficto, use the following `pip` command:
`pip install ficto`

Generate a dataset by providing a YAML configuration file, the number of rows, and the desired file format. For example, to generate a CSV file with 100 rows using a configuration file named config.yaml, run the following command:
`ficto -d config.yaml -n 100 -f csv`

## Features
* **Flexible Configuration:** Customize your dataset by defining columns and their types in a YAML file.
* **Multiple Formats:** Generate datasets in either CSV or JSON format.
* **Easy Installation:** Install Ficto effortlessly with a single pip command.
* **Realistic Demo Data:** Create realistic data for testing purpose.
* **Command-Line Interface (CLI):** User-friendly CLI for quick and simple data generation.

## Usage
1. **Create Configuration File:** Create a YAML file (e.g., config.yaml) specifying the columns and their types.

You can find a template [here](https://github.com/taeefnajib/ficto/blob/main/config-template.yaml) containing all the types of column you can add to your dataset. To know more about each value type, kindly read the documentation.

2. **Generate Data:** Use the Ficto CLI to generate data based on your configuration.

`ficto -d config.yaml -n 100 -f csv`

This command generates a CSV file inside a newly created `data` folder with 100 rows of demo data based on your data configuration file (i.e.`config.yaml`).

## Documentation
For more details and advanced usage, refer to the Ficto Documentation.

## License
This project is licensed under the [MIT License](https://github.com/taeefnajib/ficto/blob/main/LICENSE)