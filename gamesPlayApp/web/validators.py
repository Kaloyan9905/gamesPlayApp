from django.core.exceptions import ValidationError


def age_validator(value):
    if value < 12:
        raise ValidationError('Age has to be above 12!')


def rating_validator(value):
    if not 0.1 <= value <= 5.0:
        raise ValidationError('Rating has to be between 0.1 and 5.0!')


def max_level_validator(value):
    if value < 1:
        raise ValidationError('Max level has to be above 1!')
