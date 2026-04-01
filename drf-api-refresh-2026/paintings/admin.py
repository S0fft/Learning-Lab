from django.contrib import admin

from .models import Category, Painting

admin.site.register(Painting)
admin.site.register(Category)
