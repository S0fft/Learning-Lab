from django.db import models


class Painting(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    category_name = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title or f'Unnamed: {self.time_create}'


class Category(models.Model):
    title = models.CharField(max_length=256)

    def __str__(self):
        return self.title or f'Unnamed category'
