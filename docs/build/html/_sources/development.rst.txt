Development
===========

If you want to contribute to Django Country Kit, follow these steps to set up your development environment:

1. Install pipenv if you haven't already:

    .. code-block:: bash

        pip install pipenv

2. Clone the repository:

    .. code-block:: bash

        git clone https://github.com/your_username/django-country-kit.git

3. Navigate to the project directory:

    .. code-block:: bash

        cd django-country-kit

4. Install development dependencies:

    .. code-block:: bash

        pipenv install --dev

5. Activate the virtual environment:

    .. code-block:: bash

        pipenv shell

6. Run migrations:

    .. code-block:: bash

        python manage.py migrate

7. Run collectstatic:

    .. code-block:: bash

        python manage.py collectstatic

8. Start the development server:

    .. code-block:: bash

        python manage.py runserver
