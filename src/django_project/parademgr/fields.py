import re

from django.core.exceptions import ValidationError
from django.db import models


# Validator function to validate US phone number format
def validate_us_phone_number(value):
    # Regular expression to match US phone number format (e.g., (123) 456-7890 or 123-456-7890)
    phone_number_pattern = re.compile(r"^(\(\d{3}\)\s|\d{3}-)\d{3}-\d{4}$")
    if not phone_number_pattern.match(value):
        raise ValidationError(f"{value} is not a valid US phone number.")


class UsPhoneNumberField(models.CharField):
    def __init__(self, *args, **kwargs):
        # Set max_length to 14 to account for formatted phone numbers like (123) 456-7890
        kwargs["max_length"] = 14
        super().__init__(*args, **kwargs)

    def clean(self, value, model_instance):
        # Call the parent class's clean method to get the value
        value = super().clean(value, model_instance)

        # Perform validation
        validate_us_phone_number(value)

        # Return the cleaned (and validated) value
        return value
