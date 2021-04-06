from django.db import models
from django.utils.translation import gettext as _

class SquirrelTracker(models.Model):
    X = models.FloatField (
        help_text = ('Longitude'),
        )

    Y = models.FloatField(
        help_text = ('Latitude'),
        )

    Unique_Sq uirrel_ID = models.CharField(
        help_text = ('Unique Squirrel ID'),
        max_length = 50,
        unique = True,
        primary_key=True,
        )
