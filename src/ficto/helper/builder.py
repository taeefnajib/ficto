import random
from datetime import datetime, timedelta
import string
from itertools import count

from ficto.helper.data_module import *


# Function to generate a random first name
def generate_first_name(gender=None, male_names=male_names, female_names=female_names):
    """
    Generate a random first name.

    Parameters:
    - gender (str, optional): Specify the gender for the generated name ("male" or "female").
    - male_names (list, optional): List of male first names. Default is None.
    - female_names (list, optional): List of female first names. Default is None.

    Returns:
    - str: A randomly generated first name based on the specified gender.
    """
    if gender == "male":
        return random.choice(male_names)
    elif gender == "female":
        return random.choice(female_names)
    else:
        return random.choice(male_names + female_names)


# Function to generate a random last name
def generate_last_name(last_names=last_names):
    """
    Generate a random last name.

    Parameters:
    - last_names (list, optional): List of last names. Default is None.

    Returns:
    - str: A randomly generated last name.
    """
    return random.choice(last_names)


# Function to generate a random gender
def generate_gender(first_name=None, male_names=male_names, female_names=female_names):
    """
    Generate a random gender based on the provided first name or randomly if no name is provided.

    Parameters:
    - first_name (str, optional): First name to determine the gender. Default is None.
    - male_names (list, optional): List of male first names. Default is None.
    - female_names (list, optional): List of female first names. Default is None.

    Returns:
    - str: A randomly generated gender ("Male" or "Female").
    """
    male_names = set(male_names)
    female_names = set(female_names)

    # If a first name is provided and recognized
    if first_name:
        if first_name in male_names:
            return "Male"
        else:
            return "Female"

    # If no first name is provided or if the name is not recognized
    return random.choice(["Male", "Female"])


# Function to generate a random currency based on country
def generate_currency(country=None):
    """
    Generate a random currency code based on the provided country.

    Parameters:
    - country (str, optional): Country code. Default is None.

    Returns:
    - str: Randomly generated currency code. Defaults to "USD" if no country is specified.
    """
    if country:
        return country_to_currency.get(country, "USD")
    else:
        return "USD"


# Function to generate a random phone number
def generate_phone_number(country_code="US", phone_formats=phone_formats):
    """
    Generate a random phone number based on the specified country code and phone number format.

    Parameters:
    - country_code (str, optional): Country code for the phone number. Default is "US".
    - phone_formats (dict, optional): Dictionary containing phone number formats for different countries. Default is phone_formats.

    Returns:
    - str: Randomly generated phone number.
    """
    format_string = phone_formats.get(country_code, phone_formats["US"])
    # Replace each 'X' with a random digit
    phone_number = "".join(
        random.choice("0123456789") if c == "X" else c for c in format_string
    )

    return phone_number


# Function to generate a random date
def generate_random_date(start="01/01/1900", end="31/12/2023"):
    """
    Generate a random date within the specified date range.

    Parameters:
    - start (str, optional): Start date in the format "DD/MM/YYYY". Default is "01/01/1900".
    - end (str, optional): End date in the format "DD/MM/YYYY". Default is "31/12/2023".

    Returns:
    - datetime: Randomly generated date.
    """
    start = datetime.strptime(start, "%d/%m/%Y")
    end = datetime.strptime(end, "%d/%m/%Y")
    delta = end - start
    random_days = random.randrange(delta.days)
    return start + timedelta(days=random_days)


# Function to generate a random integer between start and end (inclusive)
def generate_customint(start=0, end=100, round_digits=1):
    """
    Generate a random integer within the specified range.

    Parameters:
    - start (int, optional): Start of the range (inclusive). Default is 0.
    - end (int, optional): End of the range (inclusive). Default is 100.
    - round_digits (int, optional): Number of digits to round to. Default is 1.

    Returns:
    - int: Randomly generated integer.
    """
    value = random.randint(start, end)
    return round(value / round_digits) * round_digits


# Function to generate a random float between start and end (inclusive)
def generate_customfloat(start=0.0, end=100.0, round_digits=2):
    """
    Generate a random float within the specified range.

    Parameters:
    - start (float, optional): Start of the range (inclusive). Default is 0.0.
    - end (float, optional): End of the range (inclusive). Default is 100.0.
    - round_digits (int, optional): Number of digits to round to. Default is 2.

    Returns:
    - float: Randomly generated float.
    """
    value = random.uniform(start, end)
    return round(value, round_digits)


# Function to generate a random string from a list of values
def generate_customlist(values):
    """
    Generate a random string from a given list of values.

    Parameters:
    - values (list): List of values to choose from.

    Returns:
    - str: Randomly chosen value from the list.
    """
    return random.choice(values)


# Function to generate a random unique ID based on character limit and numeric flag
def generate_customuuid(characterlimit=10, numeric=False):
    """
    Generate a random unique ID based on the specified character limit and numeric flag.

    Parameters:
    - characterlimit (int, optional): Maximum length of the generated ID. Default is 10.
    - numeric (bool, optional): If True, generate a numeric ID. Default is False.

    Returns:
    - str: Randomly generated unique ID.
    """
    if numeric:
        return "".join(random.choice(string.digits) for _ in range(characterlimit))
    else:
        return "".join(
            random.choice(string.ascii_letters + string.digits)
            for _ in range(characterlimit)
        )


# Function to generate a random "lorem ipsum" text up to the character limit
def generate_customlorem(characterlimit=200):
    """
    Generate a random "lorem ipsum" text up to the specified character limit.

    Parameters:
    - characterlimit (int, optional): Maximum length of the generated text. Default is 200.

    Returns:
    - str: Randomly generated "lorem ipsum" text.
    """
    lorem_ipsum = (
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
        "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. "
        "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. "
        "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    )
    startchar = random.randint(0, characterlimit)
    lorem_ipsum = lorem_ipsum[startchar : (startchar + characterlimit)]
    # Capitalize the first letter
    lorem_ipsum = lorem_ipsum[0].capitalize() + lorem_ipsum[1:]
    return lorem_ipsum


# Function to generate a random email address using meaningful words
def generate_email(
    emailproviders=["gmail.com", "yahoo.com", "hotmail.com", "live.com", "outlook.com"]
):
    """
    Generate a random email address using meaningful words and a randomly selected email provider.

    Parameters:
    - emailproviders (list, optional): List of email providers. Default is ["gmail.com", "yahoo.com", "hotmail.com", "live.com", "outlook.com"].

    Returns:
    - str: Randomly generated email address.
    """
    # Randomly select an email provider from the list
    provider = random.choice(emailproviders)

    # Randomly select one meaningful word from each list
    word1 = random.choice(email_1)
    word2 = random.choice(email_2)
    word3 = random.choice(email_3)
    newlist = [word1, word2, word3]
    word4 = random.choice(newlist)
    word5 = random.choice(newlist)
    while word5 == word4:
        word5 = random.choice(newlist)

    # Combine the words and email provider to create the email address
    email = f"{word4}{word5}@{provider}"

    return email


# Function to generate a random web URL with a meaningful word and domain
def generate_website(domain=[".com"]):
    """
    Generate a random web URL with a meaningful word, domain, and 'www.'.

    Parameters:
    - domain (list, optional): List of domain extensions. Default is [".com"].

    Returns:
    - str: Randomly generated web URL.
    """
    # Randomly select a meaningful word from the prefix and suffix lists
    selected_prefix = random.choice(company_prefix)
    selected_suffix = random.choice(company_suffix)

    # Randomly select a domain from the list
    selected_domain = random.choice(domain)

    # Combine the meaningful word, domain, and 'www.' to create the web URL
    url = f"www.{selected_prefix}{selected_suffix}{selected_domain}"

    return url


# Function to generate a random meaningful company name
def generate_company_name():
    """
    Generate a random meaningful company name.

    Returns:
    - str: Randomly generated company name.
    """
    # Randomly select a prefix and a suffix
    selected_prefix = random.choice(company_prefix)
    selected_suffix = random.choice(company_suffix)

    # Combine the prefix and suffix to create the company name
    company_name = f"{selected_prefix.capitalize()} {selected_suffix.capitalize()}"

    return company_name


# Function to generate a random department
def generate_department(customdept=None, default_departments=default_departments):
    """
    Generate a random department name.

    Parameters:
    - customdept (list, optional): List of custom department names. Default is None.
    - default_departments (list, optional): List of default department names. Default is default_departments.

    Returns:
    - str: Randomly generated department name.
    """
    if customdept:
        return random.choice(customdept)
    else:
        # Default list of departments
        return random.choice(default_departments)


# Function to generate a random designation
def generate_designation(customdes=None, department=None):
    """
    Generate a random job designation.

    Parameters:
    - customdes (list, optional): List of custom job designations. Default is None.
    - department (str, optional): Department name to determine relevant designations. Default is None.

    Returns:
    - str: Randomly generated job designation.
    """
    if customdes:
        return random.choice(customdes)
    elif department:
        relevant_designations = designation_mapping.get(department, [])
        if relevant_designations:
            return random.choice(relevant_designations)
    # If no customdes or relevant designations found, return a default value
    return "Employee"


# Function to generate a random passport number based on country
def generate_passport_number(country_code="US"):
    """
    Generate a random passport number based on the specified country code.

    Parameters:
    - country_code (str, optional): Country code. Default is "US".

    Returns:
    - str: Randomly generated passport number.
    """
    # Check if the country code has a specific format defined
    if country_code in passport_formats:
        format_string = passport_formats[country_code]
    else:
        # Use a default format if no specific format is defined
        format_string = "AA######"

    # Generate a random passport number based on the format
    passport_number = ""
    for char in format_string:
        if char == "A":
            passport_number += random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        elif char == "#":
            passport_number += random.choice("0123456789")
        else:
            passport_number += char  # Keep non-placeholder characters as they are

    return passport_number


# Function to generate a random SSN based on country
def generate_ssn(country_code="US"):
    """
    Generate a random Social Security Number (SSN) based on the specified country code.

    Parameters:
    - country_code (str, optional): Country code. Default is "US".

    Returns:
    - str: Randomly generated SSN.
    """
    # Check if the country code has a specific format defined
    if country_code in ssn_formats:
        format_string = ssn_formats[country_code]
    else:
        # Use a default format if no specific format is defined
        format_string = "###-##-####"

    # Generate a random SSN based on the format
    ssn = ""
    for char in format_string:
        if char == "#":
            ssn += random.choice("0123456789")
        else:
            ssn += char  # Keep non-placeholder characters as they are

    return ssn


# Function to generate a random credit card number
def generate_credit_card():
    """
    Generate a random credit card number (simplified example).

    Returns:
    - str: Randomly generated credit card number.
    """
    # Generate a random credit card number (this is a simplified example)
    card_number = "".join(random.choice("0123456789") for _ in range(16))
    return card_number


# Function to generate a random password
def generate_password():
    """
    Generate a random password.

    Returns:
    - str: Randomly generated password.
    """
    # Randomly select words from both lists
    word1 = random.choice(password_words_1)
    word2 = random.choice(password_words_2)

    # Combine the words
    password = f"{word1}{word2}"

    # Add uppercase and lowercase letters to the password
    password += random.choice(string.ascii_uppercase)
    password += random.choice(string.ascii_lowercase)

    # Generate additional random characters to reach a length between 8 and 16
    while len(password) < 8:
        password += random.choice(string.ascii_letters + string.digits)

    return password


# Function to generate a random address based on the country
def generate_address(country="US"):
    """
    Generate a random address based on the specified country.

    Parameters:
    - country (str, optional): Country code. Default is "US".

    Returns:
    - str: Randomly generated address.
    """
    # Get the states/counties and cities for the chosen country
    states_and_cities = country_to_states_and_cities.get(country, {})

    if not states_and_cities:
        return "Invalid country"

    state = random.choice(list(states_and_cities.keys()))
    cities = states_and_cities[state]
    city = random.choice(cities)

    if country == "US":
        postcode = f"{random.randint(10000, 99999)}"
    elif country == "UK":
        postcode = f"{random.choice(['AB', 'AL', 'B', 'BA', 'BB', 'BD', 'BH', 'BL', 'BN', 'BR', 'BS', 'BT', 'CA', 'CB', 'CF', 'CH', 'CM', 'CO', 'CR', 'CT', 'CV', 'CW', 'DA', 'DD', 'DE', 'DG', 'DH', 'DL', 'DN', 'DT', 'DY', 'E', 'EC', 'EH', 'EN', 'EX', 'FK', 'FY', 'G', 'GL', 'GY', 'GU', 'HA', 'HD', 'HG', 'HP', 'HR', 'HS', 'HU', 'HX', 'IG', 'IM', 'IP', 'IV', 'JE', 'KA', 'KT', 'KW', 'KY', 'L', 'LA', 'LD', 'LE', 'LL', 'LN', 'LS', 'LU', 'M', 'ME', 'MK', 'ML', 'N', 'NE', 'NG', 'NN', 'NP', 'NR', 'NW', 'OL', 'OX', 'PA', 'PE', 'PH', 'PL', 'PO', 'PR', 'RG', 'RH', 'RM', 'S', 'SA', 'SE', 'SG', 'SK', 'SL', 'SM', 'SN', 'SO', 'SP', 'SR', 'SS', 'ST', 'SW', 'SY', 'TA', 'TD', 'TF', 'TN', 'TQ', 'TR', 'TS', 'TW', 'UB', 'W','WA', 'WC', 'WD', 'WF', 'WN', 'WR', 'WS', 'WV', 'YO', 'ZE'])}{random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16'])} {random.choice(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16'])}{random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}{random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}"
    # Generate a fake street name and house/apartment number
    street = f"{random.choice(['Main','First','Park','Maple','Elm','Oak','High','Broadway','Market','Church','Washington','Central','Pine','Chestnut','Grand','Cedar','Pleasant','Lake','River'])} {random.choice(['Rd.', 'St.', 'Ave.', 'Blvd.', 'Sq.', 'Drive', 'Sqr.'])}"
    house_number = random.randint(1, 100)

    # Combine the address components
    address = f"{house_number} {street}, {city}, {state}, {postcode}, {country}"

    return address


# Function to generate a random latitude based on the country
def generate_latitude(country="US"):
    """
    Generate a random latitude based on the specified country.

    Parameters:
    - country (str, optional): Country code. Default is "US".

    Returns:
    - float: Randomly generated latitude.
    """
    # Get the latitude range for the specified country, default to 'US'
    latitude_range = country_latitudes.get(country, country_latitudes["US"])

    # Generate a random latitude within the specified range
    latitude = round(random.uniform(*latitude_range), 6)

    return latitude


# Function to generate a random longitude based on the country
def generate_longitude(country="US"):
    """
    Generate a random longitude based on the specified country.

    Parameters:
    - country (str, optional): Country code. Default is "US".

    Returns:
    - float: Randomly generated longitude.
    """
    # Get the longitude range for the specified country, default to 'US'
    longitude_range = country_longitudes.get(country, country_longitudes["US"])

    # Generate a random longitude within the specified range
    longitude = round(random.uniform(*longitude_range), 6)

    return longitude


# Function to generate a custom sequential column
def generate_custom_sequence(start=1, step=1, num_rows=100):
    """
    Generate a custom sequential column.

    Parameters:
    - start (int, optional): Starting value of the sequence. Default is 1.
    - step (int, optional): Step between each value in the sequence. Default is 1.
    - num_rows (int, optional): Number of rows in the sequence. Default is 100.

    Returns:
    - list: List of sequential values.
    """
    counter = count(start=start, step=step)
    return [next(counter) for _ in range(num_rows)]


# Function to generate a custom industry
def generate_industry(custom_industry=None):
    """
    Generate a random industry.

    Parameters:
    - custom_industry (list, optional): List of custom industry names. Default is None.

    Returns:
    - str: Randomly generated industry name.
    """
    if custom_industry:
        return random.choice(custom_industry)
    else:
        return random.choice(default_industry)


# Function to generate custom time
def generate_custom_time(start, end, num_rows, clock_type=24):
    """
    Generate custom time values.

    Parameters:
    - start (str): Start time in the format "HH:MM:SS".
    - end (str): End time in the format "HH:MM:SS".
    - num_rows (int): Number of time values to generate.
    - clock_type (int, optional): Type of clock (12 or 24). Default is 24.

    Returns:
    - list: List of randomly generated time values.
    """
    data = []
    if clock_type == 12:
        time_format = "%I:%M:%S %p"  # 12-hour clock format with AM/PM
    elif clock_type == 24:
        time_format = "%H:%M:%S"  # 24-hour clock format
    else:
        raise ValueError("Invalid clock_type. Use 12 or 24.")

    # Convert start and end times to datetime objects
    start_time = datetime.strptime(start, "%H:%M:%S")
    end_time = datetime.strptime(end, "%H:%M:%S")

    # Calculate the time difference in seconds
    time_difference = (end_time - start_time).total_seconds()

    # Generate random times within the specified range
    for _ in range(num_rows):
        random_seconds = random.uniform(0, time_difference)
        new_time = start_time + timedelta(seconds=random_seconds)
        data.append(new_time.strftime(time_format))

    return data


# Function to generate custom years
def generate_custom_year(start, end, num_rows):
    """
    Generate custom years.

    Parameters:
    - start (int): Start year.
    - end (int): End year.
    - num_rows (int): Number of years to generate.

    Returns:
    - list: List of randomly generated years.
    """
    data = []

    # Generate random years within the specified range
    for _ in range(num_rows):
        year = random.randint(start, end)
        data.append(year)

    return data


# Function to generate custom months
def generate_custom_month(start, end, num_rows):
    """
    Generate custom month names.

    Parameters:
    - start (int): Start month.
    - end (int): End month.
    - num_rows (int): Number of months to generate.

    Returns:
    - list: List of randomly generated month names.
    """
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    data = []

    # Generate random month names
    for _ in range(num_rows):
        month = random.randint(start, end)
        data.append(months[month - 1])

    return data


# Function to generate custom product categories
def generate_custom_prodcats(custom_categories=None):
    """
    Generate custom product categories.

    Parameters:
    - custom_categories (list, optional): List of custom product categories. Default is None.

    Returns:
    - str: Randomly generated product category.
    """
    if custom_categories is None:
        # Use the default product categories if custom_categories is not provided
        return random.choice(default_product_categories)
    else:
        # Use custom_categories if provided
        return random.choice(custom_categories)


# Function to generate product names based on the selected category
def generate_product_name(category):
    """
    Generate a product name based on the selected category.

    Parameters:
    - category (str): Product category.

    Returns:
    - str: Randomly generated product name.
    """
    if category in product_names_dict:
        return random.choice(product_names_dict[category])
    else:
        # If category is not found, choose randomly from all product names
        all_product_names = [
            name for names in product_names_dict.values() for name in names
        ]
        return random.choice(all_product_names)
