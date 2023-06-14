from django.db import models

from gamesPlayApp.web.validators import age_validator, rating_validator, max_level_validator


class Profile(models.Model):
    PASSWORD_MAX_LEN = 30
    FIRST_NAME_MAX_LEN = 30
    LAST_NAME_MAX_LEN = 30

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.IntegerField(
        null=False,
        blank=False,
        validators=(
            age_validator,
        ),
    )

    password = models.CharField(
        null=False,
        blank=False,
        max_length=PASSWORD_MAX_LEN,
    )

    first_name = models.CharField(
        null=True,
        blank=True,
        max_length=FIRST_NAME_MAX_LEN,
    )

    last_name = models.CharField(
        null=True,
        blank=True,
        max_length=LAST_NAME_MAX_LEN,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )


class Game(models.Model):
    TITLE_MAX_LEN = 30
    CATEGORY_MAX_LEN = 15

    CATEGORY_CHOICES = (
        ('Action', 'Action'),
        ('Adventure', 'Adventure'),
        ('Puzzle', 'Puzzle'),
        ('Strategy', 'Strategy'),
        ('Sports', 'Sports'),
        ('Board/Card Game', 'Board/Card Game'),
        ('Other', 'Other'),
    )

    title = models.CharField(
        null=False,
        blank=False,
        unique=True,
        max_length=TITLE_MAX_LEN,
    )

    category = models.CharField(
        null=False,
        blank=False,
        max_length=CATEGORY_MAX_LEN,
        choices=CATEGORY_CHOICES,
    )

    rating = models.FloatField(
        null=False,
        blank=False,
        validators=(
            rating_validator,
        ),
    )

    max_level = models.IntegerField(
        null=True,
        blank=True,
        validators=(
            max_level_validator,
        ),
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    summary = models.TextField(
        null=True,
        blank=True,
    )
