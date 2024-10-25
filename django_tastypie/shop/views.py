from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Course


def index(request):
    courses = Course.objects.all()

    return render(request, "shop/courses.html", {"courses": courses})


def single_course(request, course_id):
    # try:
    #     course = Course.objects.get(pk=course_id)
    #     return render(request, "shop/single_course.html", {"course": course})
    # except Course.DoesNotExist:
    #     raise Http404()

    course = get_object_or_404(Course, pk=course_id)
    return render(request, "shop/single_course.html", {"course": course})
