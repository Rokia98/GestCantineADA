from django.db import models
from base.helpers.date_time_model import DateTimeModel

# Create your models here.
class MenuModel(DateTimeModel):
    plat= models.OneToOneField('plat.platModel' , on_delete=models.CASCADE)
    date_creation = models.DateField()