from django.db import models


class Courses(models.Model):
    title = models.CharField(max_length=120)
    price = models.FloatField()
    date = models.DateField(auto_now=True)
