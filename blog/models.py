from django.db import models
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=120)
    author = models.CharField(max_length=120)
    body = models.TextField()
    time = models.TimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('blog:show_article', kwargs={'_id': self.id})

    @property
    def summary(self):
        if len(self.body) > 80:
            return self.body[:77] + '...'
        return self.body

    def __repr__(self):
        return f'This is article: {self.title}'
