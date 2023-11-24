ficto.helper package
====================

Submodules
----------

ficto.helper.builder module
---------------------------

This module contains a collection of functions that serve as builders for generating fictional data in various categories.
These functions can be used to create synthetic data for addresses, company names, credit cards, currencies, dates, departments, emails,
first names, genders, industries, last names, latitude and longitude coordinates, passport numbers, passwords, phone numbers,
product names, random dates, social security numbers (SSN), and websites.

Functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~

* `generate_address`: Generates a fictional address.
* `generate_company_name`: Generates a fictional company name.
* `generate_credit_card`: Generates a fictional credit card number.
* `generate_currency`: Generates a fictional currency code.
* `generate_custom_month`: Generates a custom month value.
* `generate_custom_prodcats`: Generates custom product categories.
* `generate_custom_sequence`: Generates a custom sequence.
* `generate_custom_time`: Generates a custom time value.
* `generate_custom_year`: Generates a custom year value.
* `generate_customfloat`: Generates a custom floating-point number.
* `generate_customint`: Generates a custom integer.
* `generate_customlist`: Generates a custom list.
* `generate_customlorem`: Generates custom Lorem Ipsum text.
* `generate_customuuid`: Generates a custom UUID.
* `generate_department`: Generates a fictional department name.
* `generate_designation`: Generates a fictional job designation.
* `generate_email`: Generates a fictional email address.
* `generate_first_name`: Generates a fictional first name.
* `generate_gender`: Generates a fictional gender.
* `generate_industry`: Generates a fictional industry category.
* `generate_last_name`: Generates a fictional last name.
* `generate_latitude`: Generates a fictional latitude coordinate.
* `generate_longitude`: Generates a fictional longitude coordinate.
* `generate_passport_number`: Generates a fictional passport number.
* `generate_password`: Generates a fictional password.
* `generate_phone_number`: Generates a fictional phone number.
* `generate_product_name`: Generates a fictional product name.
* `generate_random_date`: Generates a random date.
* `generate_ssn`: Generates a fictional Social Security Number (SSN).
* `generate_website`: Generates a fictional website URL.

Notes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
These functions are designed to facilitate the generation of diverse fictional data for testing, development, and educational purposes
within the `ficto` package.

.. automodule:: ficto.helper.builder
   :members:
   :undoc-members:
   :show-inheritance:

ficto.helper.data\_module module
--------------------------------

This module contains predefined lists and dictionaries that can be used as data sources for generating fictional data.
These data sets cover various categories such as names, countries, companies, emails, passwords, industries, and product categories.

Lists
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* `male_names`: A list of common male first names.
* `female_names`: A list of common female first names.
* `last_names`: A list of common last names.
* `country_latitudes`: A dictionary mapping country codes to latitude ranges.
* `country_longitudes`: A dictionary mapping country codes to longitude ranges.
* `company_prefix`: A list of prefixes for generating fictional company names.
* `company_suffix`: A list of suffixes for generating fictional company names.
* `email_1`, `email_2`, `email_3`: Lists of words used for generating fictional email addresses.
* `password_words_1`, `password_words_2`: Lists of common words for generating passwords.
* `default_departments`: A list of default department names.
* `default_industry`: A list of default industry categories.
* `default_product_categories`: A list of default product categories.

Dictionaries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* `country_to_code`: A dictionary mapping country names to their ISO country codes.
* `country_to_currency`: A dictionary mapping country names to their currency codes.
* `passport_formats`: A dictionary mapping country codes to passport number formats.
* `ssn_formats`: A dictionary mapping country codes to social security number formats.
* `phone_formats`: A dictionary mapping country codes to phone number formats.
* `designation_mapping`: A dictionary mapping common designations to department names.
* `country_to_states_and_cities`: A dictionary mapping country codes to their states and cities.
* `product_names_dict`: A dictionary containing product names mapped to their respective categories.


Note
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This module serves as a centralized data source for various fictional data generation tasks within the `ficto` package.

.. automodule:: ficto.helper.data_module
   :members:
   :undoc-members:
   :show-inheritance:

.. Module contents
.. ---------------

.. .. automodule:: ficto.helper
..    :members:
..    :undoc-members:
..    :show-inheritance:
