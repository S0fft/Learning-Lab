from books.views import BookAPIView
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/books/', BookAPIView.as_view())
]
