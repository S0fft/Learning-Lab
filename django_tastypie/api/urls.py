from api.models import CategoryResource, CourseResource
from django.urls import include, path
from tastypie.api import Api

api = Api(api_name='v1')
api.register(CourseResource())
api.register(CategoryResource())

urlpatterns = [
    path('', include(api.urls), name='index')
]
