from rest_framework import generics

from paintings.models import Painting
from paintings.serializers import PaintingSerializer


class PaintingAPIView(generics.ListAPIView):
    queryset = Painting.objects.all()
    serializer_class = PaintingSerializer
