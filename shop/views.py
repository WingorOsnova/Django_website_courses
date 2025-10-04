from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Category, Course


def index(requests):
    courses = Course.objects.all()
    categories = Category.objects.all()
    return render(request=requests, template_name='shop/courses.html', context={'courses': courses})


def single_course(requests, course_id):
    # OPTION 1
    #    try:
    #        course = Course.objects.get(pk=course_id)
    #        return render(request=requests, template_name='single_course.html', context={'course': course})
    #    except Course.DoesNotExist:
    #        raise Http404()
    # OPTION 2
    course = get_object_or_404(Course, pk=course_id)
    return render(request=requests, template_name='shop/single_course.html', context={'course': course})
