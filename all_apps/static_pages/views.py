from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from course.models import CourseHead


class HomePage(View):
    def __init__(self):
        self.template_name = 'pages/home.html'
    
    @method_decorator(login_required(login_url='signup'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        # course_object = get_object_or_404(CourseHead)
        course_head = CourseHead
        courses = CourseHead.objects.all()

        
        context = {'courses':courses}
        return render(request, self.template_name, context)

class About(View):
    def __init__(self):
        self.template_name = 'pages/about.html'
    
    @method_decorator(login_required(login_url='signup'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):

        return render(request, self.template_name)