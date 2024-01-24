"""
Django admin configuration for managing ExampleModel.

This file contains the necessary configuration to register the ExampleModel
with the Django admin interface. It uses the 'admin.site.register' function to
make the model accessible and manageable through the Django admin site.

Usage:
- Import this module in your Django project.
- Make sure 'ExampleModel' is defined in the '.models' module of the same app.

Example:
    # Import the admin module in your Django project's admin.py file.
    from django.contrib import admin

    # Import the ExampleModel from the same app's models module.
    from .models import ExampleModel

    # Register the ExampleModel with the Django admin site.
    admin.site.register(ExampleModel)
"""
from django.contrib import admin

from .models import ExampleModel

# Register your models here.
admin.site.register(ExampleModel)
