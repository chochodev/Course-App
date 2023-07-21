from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import *


class Courses(View):
    def __init__(self):
        self.template_name = 'course/courses.html'
    
    @method_decorator(login_required(login_url='signup'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        course_head = CourseHead
        courses = CourseHead.objects.all()

        
        context = {'courses':courses}
        return render(request, self.template_name, context)

class Course(View):
    def __init__(self):
        self.template_name = 'course/course.html'
    
    @method_decorator(login_required(login_url='signup'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):

        return redirect('courses')

    def post(self, request):
        data_received = list(request.POST)[1]
        if data_received:
            
            course_head = CourseHead.objects.get(slug=data_received)
            course_sections = course_head.coursesection_set.all()

            print(f'Course Heads\n\t{course_head} \n\t {type(course_head)}')
            print(f'Course Sections \n\t{list(course_sections)} \n\t {type(course_sections)}')

            for section in list(course_sections):
                course_contents = section.coursecontent_set.all()
                if course_contents:
                    print(f'Course Contents \n{course_contents}')
            # print(f'\t{list(course_contents)} \n\t {type(course_contents)}')
            
            context = {'course_head':course_head, 'course_sections':course_sections, 'course_contents':course_contents}
            return render(request, self.template_name, context)

class Notification(View):
    def __init__(self):
        self.template_name = 'course/notification.html'
    
    @method_decorator(login_required(login_url='signup'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):

        return render(request, self.template_name)

