from django.db import models

# Create your models here.
from django.db import models
from base.helpers.date_time_model import DateTimeModel

# Create your models here.
class PlatModel(DateTimeModel):
    name = models.CharField(max_length=150)
    summary =models.CharField(max_length=150)