from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class asd(models.Model):
    vacation = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    middlename = models.CharField(max_length=250)
    surrname = models.CharField(max_length=250)
    number = models.IntegerField()
    emails = models.EmailField()
    date_ofbirth = models.CharField(max_length=50)
    residential_address = models.CharField(max_length=250)
    criminal_record = models.CharField(max_length=250)
    description = models.CharField(max_length=250)

    class Meta:
        verbose_name = 'Vacancy'
        verbose_name_plural = 'Vacancys'
