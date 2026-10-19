from django.contrib import admin
from django.urls import path

from paintings.views import PaintingAPIView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/paintings_list/", PaintingAPIView.as_view()),
]
