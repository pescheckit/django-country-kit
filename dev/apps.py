"""
Django AppConfig for the 'dev' app.

This AppConfig class defines configuration settings for the 'dev' app in a Django project.
It sets the default_auto_field to 'django.db.models.BigAutoField', which is the default
AutoField for models in Django 3.2 and later versions.

Usage:
- Include the name of this AppConfig class in the 'INSTALLED_APPS' list of your Django project's settings.

Example:
    # In your Django project's settings.py file:
    INSTALLED_APPS = [
        # ... other apps
        'dev.apps.DevConfig',  # Include the AppConfig class
    ]

Attributes:
    - default_auto_field (str): The default AutoField to use for model fields.
    - name (str): The name of the app.

Note:
    This AppConfig class is automatically generated when you create a new app using the
    'python manage.py startapp' command in Django.

For more information, see Django documentation on AppConfig:
https://docs.djangoproject.com/en/5.0/ref/applications/#configuring-applications
"""

from django.apps import AppConfig


class DevConfig(AppConfig):
    """
    AppConfig class for the 'dev' app.

    Attributes:
        - default_auto_field (str): The default AutoField to use for model fields.
        - name (str): The name of the app.
    """
    default_auto_field = "django.db.models.BigAutoField"
    name = "dev"
