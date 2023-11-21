import pandas as pd
import random
import yaml

from ficto.helper.data_module import *
from ficto.helper.builder import *


# Function to create dataframe from YAML configuration
def create_dataframe(dataconfig, numrows):
    """
    Create a pandas DataFrame based on the configuration specified in a YAML file.

    Parameters:
    - dataconfig (str): Path to the YAML configuration file.

    Returns:
    - pd.DataFrame: DataFrame generated based on the configuration.
    """
    with open(dataconfig, "r") as file:
        config = yaml.safe_load(file)

    columns = config["columns"]

    data = {}

    country_col = next((col for col in columns if col["type"] == "country"), None)
    first_name_col = next((col for col in columns if col["type"] == "firstname"), None)
    department_col = next((col for col in columns if col["type"] == "department"), None)
    prodcat_col = next((col for col in columns if col["type"] == "prodcat"), None)

    # Generate first_name and country columns first if they exist
    for column in columns:
        col_name = column["name"]
        col_type = column["type"]

        if col_type == "firstname":
            data[col_name] = [generate_first_name() for _ in range(numrows)]
        elif col_type == "country":
            country_list = column.get("countries", ["US"])
            data[col_name] = [random.choice(country_list) for _ in range(numrows)]
        elif col_type == "department":
            custom_departments = column.get("customdept")
            data[col_name] = [
                generate_department(custom_departments) for _ in range(numrows)
            ]
        elif col_type == "prodcat":
            # If the column type is "prodcat," generate product categories
            custom_categories = column.get("customcats", None)
            data[col_name] = [
                generate_custom_prodcats(custom_categories) for _ in range(numrows)
            ]

    # Generate other columns
    for column in columns:
        col_name = column["name"]
        col_type = column["type"]
        col_datatype = column.get("datatype", "string")

        # Check if the column is already generated
        if col_name in data:
            continue

        if col_type == "gender":
            # Use first names to generate genders, if first_name column exists
            if first_name_col:
                first_names = data.get(first_name_col["name"], [None] * numrows)
                data[col_name] = [generate_gender(name) for name in first_names]
            else:
                # Generate random genders if first_name column does not exist
                data[col_name] = [generate_gender() for _ in range(numrows)]
        elif col_type == "lastname":
            lastnames = column.get("lastnames", None)
            data[col_name] = [generate_last_name() for _ in range(numrows)]
        elif col_type == "phonenumber":
            if country_col:
                # If country column exists, use country names to determine country codes
                countries = data.get(country_col["name"], ["US"] * numrows)
                country_codes = [
                    country_to_code.get(country, "US") for country in countries
                ]
                data[col_name] = [generate_phone_number(code) for code in country_codes]
            else:
                # Default to 'US' if no country column
                data[col_name] = [generate_phone_number("US") for _ in range(numrows)]
        elif col_type == "country":
            country_list = column.get("countries", ["US"])
            data[col_name] = [random.choice(country_list) for _ in range(numrows)]
        elif col_type == "customdate":
            start = column.get("start", "01/01/1900")
            end = column.get("end", "31/12/2023")
            data[col_name] = [generate_random_date(start, end) for _ in range(numrows)]
        elif col_type == "customint":
            start = column.get("start", 0)
            end = column.get("end", 100)
            round_digits = column.get("round", 1)
            data[col_name] = [
                generate_customint(start, end, round_digits) for _ in range(numrows)
            ]
        elif col_type == "customfloat":
            start = column.get("start", 0.0)
            end = column.get("end", 100.0)
            round_digits = column.get("round", 2)
            data[col_name] = [
                generate_customfloat(start, end, round_digits) for _ in range(numrows)
            ]
        elif col_type == "customlist":
            values = column.get("values", [])
            data[col_name] = [generate_customlist(values) for _ in range(numrows)]
        elif col_type == "customuuid":
            characterlimit = column.get("characterlimit", 10)
            numeric = column.get("numeric", False)
            data[col_name] = [
                generate_customuuid(characterlimit, numeric) for _ in range(numrows)
            ]
        elif col_type == "customlorem":
            characterlimit = column.get("characterlimit", 200)
            data[col_name] = [
                generate_customlorem(random.randint(20, characterlimit))
                for _ in range(numrows)
            ]
        elif col_type == "email":
            emailproviders = column.get(
                "emailprovider",
                ["gmail.com", "yahoo.com", "hotmail.com", "live.com", "outlook.com"],
            )
            data[col_name] = [generate_email(emailproviders) for _ in range(numrows)]
        elif col_type == "website":
            domain = column.get("domain", [".com"])
            data[col_name] = [generate_website(domain) for _ in range(numrows)]
        elif col_type == "organization":
            data[col_name] = [generate_company_name() for _ in range(numrows)]
        elif col_type == "designation":
            custom_designations = column.get("customdes")
            if department_col:
                data[col_name] = [
                    generate_designation(custom_designations, department)
                    for department in data["Dept"]
                ]
            else:
                data[col_name] = [
                    generate_designation(custom_designations) for _ in range(numrows)
                ]
        elif col_type == "currency":
            if country_col:
                data[col_name] = [
                    generate_currency(country) for country in data[country_col["name"]]
                ]
            else:
                data[col_name] = ["USD" for _ in range(numrows)]
        elif col_type == "passport":
            # data[col_name] = [generate_passport_number() for _ in range(numrows)]
            if country_col:
                data[col_name] = [
                    generate_passport_number(country)
                    for country in data[country_col["name"]]
                ]
            else:
                data[col_name] = [
                    generate_passport_number(country="US") for _ in range(numrows)
                ]
        elif col_type == "ssn":
            # data[col_name] = [generate_ssn() for _ in range(numrows)]
            if country_col:
                data[col_name] = [
                    generate_ssn(country) for country in data[country_col["name"]]
                ]
            else:
                data[col_name] = [generate_ssn(country="US") for _ in range(numrows)]
        elif col_type == "ccn":
            data[col_name] = [generate_credit_card() for _ in range(numrows)]
        elif col_type == "password":
            data[col_name] = [generate_password() for _ in range(numrows)]
        elif col_type == "address":
            if country_col:
                data[col_name] = [
                    generate_address(country) for country in data[country_col["name"]]
                ]
            else:
                data[col_name] = [
                    generate_address(country="US") for _ in range(numrows)
                ]
        elif col_type == "lat":
            if country_col:
                data[col_name] = [
                    generate_latitude(country) for country in data[country_col["name"]]
                ]
            else:
                # Set a default value or handle it as you prefer
                data[col_name] = [generate_latitude("US") for _ in range(numrows)]
        elif col_type == "long":
            if country_col:
                data[col_name] = [
                    generate_longitude(country) for country in data[country_col["name"]]
                ]
            else:
                # Set a default value or handle it as you prefer
                data[col_name] = [generate_longitude("US") for _ in range(numrows)]
        elif col_type == "industry":
            custom_industry = column.get("customindustry")
            data[col_name] = [
                generate_industry(custom_industry) for _ in range(numrows)
            ]
        elif col_type == "customtime":
            start = column.get("start", "08:00:00")
            end = column.get("end", "23:59:59")  # End time in 24-hour format
            clock_type = column.get("clock_type", "24")
            data[col_name] = generate_custom_time(start, end, numrows, clock_type)
        elif col_type == "customyear":
            start = column.get("start", 1900)
            end = column.get("end", 2023)
            data[col_name] = generate_custom_year(start, end, numrows)
        elif col_type == "custommonth":
            start = column.get("start", 1)
            end = column.get("end", 12)
            data[col_name] = generate_custom_month(start, end, numrows)
        elif col_type == "prodname":
            # If the column type is "prodname," generate product titles based on prodcat
            if prodcat_col:
                # product_categories = data.get(prodcat_col, [])
                # data[col_name] = [generate_product_name(category) for category in product_categories]
                data[col_name] = [
                    generate_product_name(category)
                    for category in data[prodcat_col["name"]]
                ]
            else:
                # If prodcat is not found, choose randomly from all product titles
                data[col_name] = [generate_product_name(None) for _ in range(numrows)]

        else:
            # Handle other column types if needed
            pass
        # Use the generate_custom_sequence function for customseq columns
        for column in columns:
            col_name = column["name"]
            col_type = column["type"]
            col_datatype = column.get("datatype", "string")

            if col_type == "customseq":
                start = column.get("start", 1)
                step = column.get("step", 1)
                data[col_name] = generate_custom_sequence(start, step, numrows)

        # Convert column to specified datatype
        if col_datatype == "int":
            data[col_name] = pd.to_numeric(data[col_name], errors="coerce")
        elif col_datatype == "float":
            data[col_name] = pd.to_numeric(data[col_name], errors="coerce").astype(
                float
            )
    
    df = pd.DataFrame(data)
    # Sort the columns based on the 'pos' parameter, if present
    if any("pos" in column for column in columns):
        df = df[
            [
                col
                for col in sorted(
                    df.columns,
                    key=lambda x: next(
                        (c["pos"] for c in columns if c["name"] == x), 0
                    ),
                )
            ]
        ]
    return df
