from django.db import models
from django.contrib.auth import get_user_model
from feedbac.settings import COLOR_CHOICES, TYPE_SELECT, QUESTION_SELECT


User = get_user_model()

class FeedbacksModel(models.Model):
    vacation = models.CharField(max_length=250, choices=COLOR_CHOICES)
    name = models.CharField(max_length=250)
    middlename = models.CharField(max_length=250)
    surrname = models.CharField(max_length=250, blank=True)
    number = models.IntegerField(null=True, default=None)
    emails = models.EmailField()
    date_ofbirth = models.CharField(max_length=50)
    residential_address = models.CharField(max_length=250)
    criminal_record = models.CharField(max_length=250, choices=TYPE_SELECT, default='Нет')
    description = models.CharField(max_length=250)
    response_status = models.TextField()

    class Meta:
        verbose_name = 'Vacancy'
        verbose_name_plural = 'Vacancys'

class Post(models.Model):
    vacation = models.CharField(max_length=250, choices=COLOR_CHOICES)
    question = models.CharField(max_length=250, choices=QUESTION_SELECT)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    emails = models.EmailField()
    response_status = models.TextField()

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ('-pub_date',)
