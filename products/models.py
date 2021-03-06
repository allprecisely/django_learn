from django.db import models
from django.urls import reverse


class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    summary = models.TextField(blank=True, null=True)
    featured = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('products:detail', kwargs={'_id': self.id})

    def __repr__(self):
        return f'This is product: {self.title}'
