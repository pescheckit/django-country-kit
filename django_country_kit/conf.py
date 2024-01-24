"""
AppSettings class for handling app-specific default settings.

This module defines the 'AppSettings' class, which serves as a holder for app-specific default settings.
It allows overriding these defaults via the project's settings in Django.

Usage:
- Include this module in your Django app.
- Use an instance of the 'AppSettings' class to access app-specific settings with fallbacks to project settings.

Example:
    # In your Django app's code:
    from .app_settings import settings

    app_specific_setting = settings.APP_SPECIFIC_SETTING

Attributes:
    - AppSettings (class): A class for handling app-specific default settings.
        - __getattribute__(method): Overrides the default __getattribute__ method to retrieve settings
          from Django's project settings.

    - settings (AppSettings instance): An instance of the 'AppSettings' class for accessing app-specific
      settings in your Django app.

Note:
    The 'AppSettings' class dynamically retrieves app-specific settings from the Django project's settings.
    This allows you to define default settings within the app and override them in the project's settings.

For more information, see Django documentation on settings:
https://docs.djangoproject.com/en/5.0/topics/settings/
"""

import django.conf


class AppSettings:  # pylint: disable=too-few-public-methods
    """
    A holder for app-specific default settings that allows overriding via
    the project's settings.
    """

    def __getattribute__(self, attr: str):
        """
        Overrides the default __getattribute__ method to retrieve settings
        from Django's project settings.

        Parameters:
            - attr (str): The name of the attribute to retrieve.

        Returns:
            - Any: The value of the attribute from the project's settings, or the default value.
        """
        if attr == attr.upper():
            try:
                return getattr(django.conf.settings, attr)
            except AttributeError:
                pass
        return super().__getattribute__(attr)

# An instance of the 'AppSettings' class for accessing app-specific settings.
settings = AppSettings()
