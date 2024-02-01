Installation
============

To install Django Country Kit, follow these steps:

1. Install Django Country Kit using pip:

    .. code-block:: bash

        pip install django-country-kit

2. Add `'django_country_kit'` to your `INSTALLED_APPS` in your Django project's settings:

    .. code-block:: python

        INSTALLED_APPS = [
            # ...
            'django_country_kit',
            # ...
        ]


3. Run collectstatic:

    .. code-block:: bash

        python manage.py collectstatic

