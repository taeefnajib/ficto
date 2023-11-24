Writing Data Config File
---------------------------

We have 31 types of value that can be generated.

.. _customseq:

customseq
=========

Generates a custom sequence of integers.

Parameters:
    - `start` (optional): Starting value of the sequence (default: 1).
    - `step` (optional): Step size between values (default: 1).

Example:
^^^^^^^^

.. code-block:: yaml

    type: customseq
    datatype: int
    start: 1
    step: 1
    name: 'ID'
    pos: 1


.. _firstname:

firstname
=========

Generates random first names.

Parameters:
    None.

Example:
^^^^^^^^

.. code-block:: yaml

    type: firstname
    datatype: string
    name: 'First Name'
    pos: 2


.. _lastname:

lastname
========

Generates random last names.

Parameters:
    None.

Example:
^^^^^^^^

.. code-block:: yaml

    type: lastname
    datatype: string
    name: 'Last Name'
    pos: 3


.. _gender:

gender
======

Generates random gender values.

Parameters:
    None.

Example:
^^^^^^^^

.. code-block:: yaml

    type: gender
    datatype: string
    name: 'Gender'
    pos: 4


.. _country:

country
=======

Generates random country names.

Parameters:
    - `countries` (optional): List of specific countries to choose from (default: ['US']).

Example:
^^^^^^^^

.. code-block:: yaml

    type: country
    datatype: string
    countries: ['US','UK']
    name: 'Country'
    pos: 5


.. _phonenumber:

phonenumber
===========

Generates random phone numbers.

Parameters:
    None.

Example:
^^^^^^^^

.. code-block:: yaml

    type: phonenumber
    datatype: string
    name: 'Phone No.'
    pos: 6


.. _currency:

currency
========

Generates random currency codes.

Parameters:
    - `currency` (optional): List of specific currency codes to choose from (default: ['USD']).

Example:
^^^^^^^^

.. code-block:: yaml

    type: currency
    datatype: string
    currency: ['USD', 'GBP', 'AUD', 'CAD']
    name: 'Currency'
    pos: 7


.. _customdate:

customdate
==========

Generates random dates within a specified range.

Parameters:
    - `start` (optional): Start date in 'DD/MM/YYYY' format (default: '01/01/1900').
    - `end` (optional): End date in 'DD/MM/YYYY' format (default: '31/12/2023').

Example:
^^^^^^^^

.. code-block:: yaml

    type: customdate
    datatype: datetime
    start: '01/01/1980'
    end: '31/12/2006'
    name: 'DOB'
    pos: 8


.. _customint:

customint
=========

Generates random integers within a specified range.

Parameters:
    - `start` (optional): Start value of the range (default: 0).
    - `end` (optional): End value of the range (default: 100).
    - `round` (optional): Number of decimal places to round to (default: 1).

Example:
^^^^^^^^

.. code-block:: yaml

    type: customint
    datatype: int
    start: 10000
    end: 20000
    round: 1000
    name: 'Salary'
    pos: 9


.. _customfloat:

customfloat
===========

Generates random floating-point numbers within a specified range.

Parameters:
    - `start` (optional): Start value of the range (default: 0.0).
    - `end` (optional): End value of the range (default: 100.0).
    - `round` (optional): Number of decimal places to round to (default: 2).

Example:
^^^^^^^^

.. code-block:: yaml

    type: customfloat
    datatype: float
    start: 97.5
    end: 101.5
    round: 1
    name: 'Body Temp.'
    pos: 10


.. _customlist:

customlist
==========

Generates a random value from a custom list.

Parameters:
    - `values` (required): List of values to choose from.

Example:
^^^^^^^^

.. code-block:: yaml

    type: customlist
    datatype: string
    values: ['A+', 'B+', 'AB+', 'O+', 'A-', 'B-', 'AB-', 'O-']
    name: 'Blood Group'
    pos: 11


.. _customuuid:

customuuid
==========

Generates random UUIDs.

Parameters:
    - `characterlimit` (optional): Maximum number of characters in the UUID (default: 10).
    - `numeric` (optional): If True, generate a numeric UUID; otherwise, alphanumeric (default: False).

Example:
^^^^^^^^

.. code-block:: yaml

    type: customuuid
    datatype: string
    characterlimit: 6
    numeric: True
    name: 'Employee ID'
    pos: 12


.. _customlorem:

customlorem
===========

Generates random Lorem Ipsum text.

Parameters:
    - `characterlimit` (optional): Maximum number of characters in the Lorem Ipsum text (default: 200).

Example:
^^^^^^^^

.. code-block:: yaml

    type: customlorem
    datatype: string
    characterlimit: 20
    name: 'Feedback'
    pos: 13


.. _email:

email
=====

Generates random email addresses.

Parameters:
    - `emailprovider` (optional): List of email providers to choose from.

Example:
^^^^^^^^

.. code-block:: yaml

    type: email
    datatype: string
    emailprovider: ['gmail.com','yahoo.com','hotmail.com']
    name: 'Email'
    pos: 14


.. _website:

website
=======

Generates random website URLs.

Parameters:
    - `domain` (optional): List of domain extensions to choose from (default: ['.com']).

Example:
^^^^^^^^

.. code-block:: yaml

    type: website
    datatype: string
    domain: ['.com','.net','.org']
    name: 'URL'
    pos: 15


.. _organization:

organization
=============

Generates random organization names.

Parameters:
    None.

Example:
^^^^^^^^

.. code-block:: yaml

    type: organization
    datatype: string
    name: 'Company'
    pos: 16


.. _department:

department
==========

Generates random department names.

Parameters:
    - `customdept` (optional): List of custom department names to choose from.

Example:
^^^^^^^^

.. code-block:: yaml

    type: department
    datatype: string
    customdept: ['Marketing', 'Engineering', 'HR']
    name: 'Dept'
    pos: 17


.. _designation:

designation
============

Generates random job titles.

Parameters:
    - `customdes` (optional): List of custom job titles to choose from.

Example:
^^^^^^^^

.. code-block:: yaml

    type: designation
    datatype: string
    customdes: ["Executive","Manager","Director"]
    name: 'Designation'
    pos: 18


.. _passport:

passport
=========

Generates random passport numbers.

Parameters:
    - `country` (optional): Country for which the passport number should be generated (default: 'US').

Example:
^^^^^^^^

.. code-block:: yaml

    type: passport
    datatype: string
    country: 'US'
    name: 'Passport'
    pos: 19


.. _ssn:

ssn
=====

Generates random Social Security Numbers (SSNs).

Parameters:
    - `country` (optional): Country for which the SSN should be generated (default: 'US').

Example:
^^^^^^^^

.. code-block:: yaml

    type: ssn
    datatype: string
    country: 'US'
    name: 'SSN'
    pos: 20


.. _ccn:

ccn
=====

Generates random credit card numbers.

Parameters:
    None.

Example:
^^^^^^^^

.. code-block:: yaml

    type: ccn
    datatype: string
    name: 'Credit Card'
    pos: 21


.. _password:

password
=========

Generates random passwords.

Parameters:
    None.

Example:
^^^^^^^^

.. code-block:: yaml

    type: password
    datatype: string
    name: 'Password'
    pos: 22


.. _address:

address
========

Generates random addresses.

Parameters:
    - `country` (optional): Country for which the address should be generated (default: 'US').

Example:
^^^^^^^^

.. code-block:: yaml

    type: address
    datatype: string
    country: 'US'
    name: 'Address'
    pos: 23


.. _lat:

lat
====

Generates random latitude values.

Parameters:
    - `country` (optional): Country for which the latitude should be generated (default: 'US').

Example:
^^^^^^^^

.. code-block:: yaml

    type: lat
    datatype: string
    country: 'US'
    name: 'Latitude'
    pos: 24


.. _long:

long
====

Generates random longitude values.

Parameters:
    - `country` (optional): Country for which the longitude should be generated (default: 'US').

Example:
^^^^^^^^

.. code-block:: yaml

    type: long
    datatype: string
    country: 'US'
    name: 'Longitude'
    pos: 25


.. _industry:

industry
========

Generates random industry names.

Parameters:
    - `customindustry` (optional): List of custom industry names to choose from.

Example:
^^^^^^^^

.. code-block:: yaml

    type: industry
    datatype: string
    customindustry: ['Fashion and Retail', 'Telecom', 'Technology', 'Automotive', 'Media and Entertainment']
    name: 'Industry'
    pos: 26

.. _customtime:

customtime
==========

Generates random times within a specified range.

Parameters:
    - `start` (optional): Start time (default: '08:00:00').
    - `end` (optional): End time (default: '23:59:59').
    - `clock_type` (optional): Clock type (12 or 24, default: 24).

Example:
^^^^^^^^

.. code-block:: yaml

    type: customtime
    datatype: datetime
    start: '08:00:00'
    end: '23:59:59'
    clock_type: 24
    name: 'Time of Arrival'
    pos: 27

.. _customyear:

customyear
==========

Generates random years within a specified range.

Parameters:
    - `start` (optional): Start year (default: 1900).
    - `end` (optional): End year (default: 2023).

Example:
^^^^^^^^

.. code-block:: yaml

    type: customyear
    datatype: int
    start: 1900
    end: 2023
    name: 'Year'
    pos: 28


.. _custommonth:

custommonth
============

Generates random month names or numbers.

Parameters:
    - `start` (optional): Start month (default: 1).
    - `end` (optional): End month (default: 12).

Example:
^^^^^^^^

.. code-block:: yaml

    type: custommonth
    datatype: string
    start: 1
    end: 12
    name: 'Month'
    pos: 29


.. _prodname:

prodname
========

Generates random product names.

Parameters:
    None.

Example:
^^^^^^^^

.. code-block:: yaml

    type: prodname
    datatype: string
    name: 'Product'
    pos: 30


.. _prodcat:

prodcat
=======

Generates random product categories.

Parameters:
    - `customcats` (optional): List of custom product categories to choose from.

Example:
^^^^^^^^

.. code-block:: yaml

    type: prodcat
    datatype: string
    customcats: ["Electronics", "Clothing", "Home and Kitchen", "Books", "Toys"]
    name: 'Category'
    pos: 31