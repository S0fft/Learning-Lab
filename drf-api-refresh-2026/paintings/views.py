from django.shortcuts import render
from rest_framework import generics

from .models import Painting
from .serializers import PaintingSerializer


class PaintingAPIView(generics.ListAPIView):
    queryset = Painting.objects.all()
    serializer_class = PaintingSerializer
