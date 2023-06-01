from django.db import models

class asd(models.Model):
    vacation = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    middlename = models.CharField(max_length=250)
    surrname = models.CharField(max_length=250)
    number = models.IntegerField()
    emails = models.EmailField()
    pasport_number = models.IntegerField()
    pasport_series = models.IntegerField()
    url_linc = models.URLField()
    description = models.CharField(max_length=250)

    class Meta:
        verbose_name = 'Vacancy'
        verbose_name_plural = 'Vacancys'
