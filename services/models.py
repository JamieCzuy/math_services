from django.db import models

# Create your models here.
class SquaresDifference(models.Model):

    given_number = models.PositiveIntegerField()
    value = models.PositiveIntegerField()
    occurrences = models.PositiveIntegerField()
    last_requested = models.DateTimeField(auto_now=True)