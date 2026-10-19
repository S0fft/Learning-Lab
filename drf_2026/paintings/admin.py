from django.contrib import admin

from paintings.models import Category, Painting

admin.site.register(Painting)
admin.site.register(Category)
