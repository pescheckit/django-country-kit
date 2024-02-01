Custom Settings
===============

Django Country Kit provides custom settings for further customization of country data:

- **OVERRIDE_COUNTRIES**: Allows users to override specific countries with custom data.
- **EXCLUDE_COUNTRIES**: Allows users to exclude specific countries from the available choices.
- **INCLUDE_COUNTRIES**: Allows users to include specific countries in the available choices.

Examples
--------

OVERRIDE_COUNTRIES
~~~~~~~~~~~~~~~~~~

To override specific countries with custom data, you can define the ``OVERRIDE_COUNTRIES`` setting in your Django project's settings file. Here's an example:

.. code-block:: python

    # settings.py

    OVERRIDE_COUNTRIES = {
        'US': {'name': 'United States of America', 'alpha3':'USA'},
        'GB': {'name': 'United Kingdom', 'alpha3':'GBR'},
        'CA': {'name':'Canada', 'alpha3':'CAN'}
        # Add more overrides as needed
    }

In this example, the names of the countries with codes 'US', 'GB', and 'CA' will be overridden with custom names.

EXCLUDE_COUNTRIES
~~~~~~~~~~~~~~~~~~

To exclude specific countries from the available choices, you can define the ``EXCLUDE_COUNTRIES`` setting in your Django project's settings file. Here's an example:

.. code-block:: python

    # settings.py

    EXCLUDE_COUNTRIES = ['US', 'GB', 'CA']

In this example, the countries with codes 'US', 'GB', and 'CA' will be excluded from the available choices.

INCLUDE_COUNTRIES
~~~~~~~~~~~~~~~~~~

To include specific countries in the available choices, you can define the ``INCLUDE_COUNTRIES`` setting in your Django project's settings file. Here's an example:

.. code-block:: python

    # settings.py

    INCLUDE_COUNTRIES = {
        'US': {'name': 'United States of America', 'alpha3':'USA'},
        'GB': {'name': 'United Kingdom', 'alpha3':'GBR'},
        'CA': {'name':'Canada', 'alpha3':'CAN'}
    }

In this example, only the countries with codes 'US', 'GB', and 'CA' will be included in the available choices.

You can customize these settings in your Django project's settings file to tailor the country data according to your needs.
