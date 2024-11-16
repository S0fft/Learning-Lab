from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from .models import Book

# class BookSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Book
#         fields = ('title', 'category_id',)


class BookModel:
    def __init__(self, title, content):
        self.title = title
        self.content = content


class BookSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()


def encode():
    model = BookModel('Test-1', 'Content: Test-2')
    model_sr = BookSerializer(model)
    print(model_sr.data, type(model_sr.data), sep='\n')

    json = JSONRenderer().render(model_sr.data)
    print(json)
