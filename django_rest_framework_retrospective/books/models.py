from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.title
