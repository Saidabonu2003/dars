from django.shortcuts import render, get_object_or_404
from django.http import Http404

from .models import Course, Bob
# Create your views here.

def home(request):
    courses = Course.objects.all()
    return render(request, "index.html", {"courses": courses})


def lesson(request, slug):
    try:
        course = Course.objects.get(slug=slug)
        bobs = course.bob.all()
        return render(request, "page/sidbar.html", {"course": course, "bobs": bobs})
    
    except Course.DoesNotExist as e:
        raise Http404("Topilmadi")