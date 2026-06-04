from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Painting
from .serializers import PaintingSerializer

# class PaintingAPIView(generics.ListAPIView):
#     queryset = Painting.objects.all()
#     serializer_class = PaintingSerializer


class PaintingAPIView(APIView):
    def get(self, request):
        lst = Painting.objects.all().values()

        return Response({'Painting': list(lst)})

    def post(self, request):
        new_post = Painting.objects.create(
            title=request.data['title'],
            description=request.data['description'],
            category_name_id=request.data['category_name']
        )
        return Response({'post': model_to_dict(new_post)})
