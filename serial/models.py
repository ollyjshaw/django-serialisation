from django.db import models
from django.contrib.postgres.fields import DateTimeRangeField

class SerialTest(models.Model):
  full_name = models.CharField(max_length=100)
  date_range = DateTimeRangeField()
