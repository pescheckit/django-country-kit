"""
Django forms for working with country fields.

This module provides custom form fields and widgets for working with country data in Django applications.
It includes a custom field `CountryField` that extends Django's `CharField` to handle country data efficiently.
Additionally, it includes a custom list type `MultiSelectList` used
for handling multiple selections within the `CountryField`.

Classes:
    - MultiSelectList: Represents a list with multiple selections.
    - CountryField: A custom field for storing country data.

The `CountryField` class extends Django's `CharField` to provide specialized
functionality for storing and handling country data.
It supports both single and multiple country selections,
with customizable options for the field's appearance and behavior.

The `MultiSelectList` class is a custom list type used within the `CountryField`
for managing multiple selections efficiently.
It provides methods for string representation and initialization based on a dictionary of choices.

This module is intended to be used in Django projects where country-related data needs
to be stored and managed in forms and models.

Dependencies:
    - Django: The web framework for building Django applications.
"""

from django import forms
from django.core import exceptions
from django.db.models.fields import BLANK_CHOICE_DASH, CharField

from .base import Country
from .widgets import CountryWidget, MultipleCountryWidget


class MultiSelectList(list):
    """
    A list subclass representing a multi-select list with associated choices.

    This class extends the built-in list class to provide additional functionality
    for a multi-select list, where each item in the list corresponds to a choice
    from a predefined set of choices.

    Attributes:
        choices (dict): A dictionary representing the available choices.
            The keys are the choice values, and the values are the corresponding
            choice data or descriptions.
    """
    def __init__(self, choices, *args, **kwargs):
        self.choices = choices
        super().__init__(*args, **kwargs)

    def __str__(self):
        msg_list = [self.choices.get(int(i)) if i.isdigit() else self.choices.get(i) for i in self]
        return ', '.join([str(s) for s in msg_list])


class CountryField(CharField):
    """
    A custom field for storing country data.

    Inherits from CharField.
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes a CountryField instance.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        self.countries = Country().countries_data
        self.multiple = kwargs.pop('multiple', False)
        self.blank_label = kwargs.pop("blank_label", None)

        include_blank = kwargs.get('blank', False)

        self.choices = kwargs.pop("countries", None)
        if not self.choices:
            self.choices = self.get_choices(include_blank=include_blank)

        kwargs['choices'] = self.choices
        if self.multiple:
            kwargs['max_length'] = len(self.countries) - 1 + sum(len(code) for code in self.countries)
        else:
            kwargs['max_length'] = max(len(code) for code in self.countries)
        super().__init__(*args, **kwargs)

    def get_choices(self, *_args, include_blank=True, blank_choice=None, **_kwargs):
        """
        Returns choices with an optional blank choice if include_blank=True.
        """
        if self.multiple:
            include_blank = False

        if include_blank:
            if blank_choice is None:
                blank_choice = [("", self.blank_label)] if self.blank_label else BLANK_CHOICE_DASH
        else:
            blank_choice = []

        choices = blank_choice + [(code, data['name']) for code, data in self.countries.items()]

        return choices

    def get_choices_selected(self, arr_choices):
        """
        Retrieve selected choices from an array of choices.

        Args:
            arr_choices (list): A list of tuples where each tuple represents a choice.
                Each choice tuple should have the format (choice_value, choice_data),
                where choice_value is the value of the choice and choice_data is optional.

        Returns:
            list: A list of selected choice values converted to strings.
        """
        named_groups = arr_choices and isinstance(arr_choices[0][1], (list, tuple))
        choices_selected = []
        if named_groups:
            for choice_group_selected in arr_choices:
                for choice_selected in choice_group_selected[1]:
                    choices_selected.append(str(choice_selected[0]))
        else:
            for choice_selected in arr_choices:
                choices_selected.append(str(choice_selected[0]))
        return choices_selected

    def value_to_string(self, obj):
        try:
            value = self._get_val_from_obj(obj)
        except AttributeError:
            value = super().value_from_object(obj)
        return self.get_prep_value(value)

    def validate(self, value, model_instance):  # pylint: disable=inconsistent-return-statements
        if not self.multiple:
            return super().validate(value, model_instance)
        arr_choices = self.get_choices_selected(self.get_choices(include_blank=False))
        for opt_select in value:
            if opt_select not in arr_choices:
                raise exceptions.ValidationError(self.error_messages['invalid_choice'] % {"value": value})

    def get_default(self):
        default = super().get_default()
        if not self.multiple:
            return default
        if isinstance(default, int):
            default = str(default)
        return default

    def formfield(self, **kwargs):
        defaults = {
            'required': not self.blank,
            'help_text': self.help_text,
            'choices': self.choices,
            'widget': CountryWidget if not self.multiple else MultipleCountryWidget,
        }
        if self.has_default():
            defaults['initial'] = self.get_default()
        defaults.update(kwargs)
        if self.multiple:
            return forms.TypedMultipleChoiceField(**defaults)
        return forms.TypedChoiceField(**defaults)

    def get_prep_value(self, value):
        if not self.multiple:
            return super().get_prep_value(value)
        return '' if value is None else ",".join(map(str, value))

    def get_db_prep_value(self, value, connection, prepared=False):
        if not self.multiple:
            return super().get_db_prep_value(value, connection, prepared)
        if not prepared and not isinstance(value, str):
            value = self.get_prep_value(value)
        return value

    def to_python(self, value):
        if not self.multiple:
            return super().to_python(value)
        choices = dict(self.flatchoices)

        if value:
            if isinstance(value, list):
                return value
            if isinstance(value, str):
                value_list = map(lambda x: x.strip(), value.replace('，', ',').split(','))
                return MultiSelectList(choices, value_list)
            if isinstance(value, (set, dict)):
                return MultiSelectList(choices, list(value))
        return MultiSelectList(choices, [])

    def from_db_value(self, value, expression, connection):  # pylint: disable=unused-argument
        """
        Convert a database value to a Python object.

        This method is used by Django to convert a value fetched from the database
        into the appropriate Python object before assigning it to the model field.

        Args:
            value: The database value to be converted.
            expression: The database expression used in the query.
            connection: The database connection.

        Returns:
            The Python object representing the converted value.

        Note:
            This method is primarily used in custom model fields.
        """
        if value is None:
            return value
        return self.to_python(value)

    def contribute_to_class(self, cls, name, private_only=False):
        super().contribute_to_class(cls, name)

        if not self.multiple:
            return

        if self.choices:
            choicedict = dict(self.choices)

            def get_list(obj):
                field_value = getattr(obj, name)
                if field_value:
                    display = [str(choicedict.get(value, value)) for value in field_value]
                    return display
                return []

            def get_display(obj):
                return ", ".join(get_list(obj))

            get_display.short_description = self.verbose_name

            setattr(cls, f'get_{self.name}_list', get_list)
            setattr(cls, f'get_{self.name}_display', get_display)
