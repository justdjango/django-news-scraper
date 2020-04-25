from django.db import models


class NewsItem(models.Model):
    source = models.CharField(max_length=100)  # Medium / Dev.to
    link = models.TextField()
    title = models.CharField(max_length=200)
    publish_date = models.DateField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.link[0:50]
