from django.forms import model_to_dict
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Book
from .serializers import BookSerializer

# class BookAPIView(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


class BookAPIView(APIView):
    def get(self, request):
        # lst = Book.objects.all().values()
        books = Book.objects.all()

        return Response({'posts': BookSerializer(books, many=True).data})

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        post_new = Book.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            category_id=request.data['category_id']
        )

        return Response({'post': BookSerializer(post_new).data})
