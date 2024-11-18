import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Book

# class BookSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Book
#         fields = ('title', 'category_id',)


# class BookModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content


# class BookSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=255)
#     content = serializers.CharField()


# def encode():
#     model = BookModel('Test1', 'Content: Test1')
#     model_sr = BookSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')

#     json = JSONRenderer().render(model_sr.data)
#     print(json)


# def decode():
#     stream = io.BytesI0(b'{"title":"Test2", "content":"Test2"}')
#     data = JSONParser().parse(stream)
#     serializer = BookSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validate_data)

class BookSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    category_id = serializers.IntegerField()
    content = serializers.CharField()
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=True)
