from django.shortcuts import render
from django.views import View


class HomePage(View):
    def __init__(self):
        self.template_name = 'course/home.html'

    def get(self, request):

        return render(request, self.template_name)

class Courses(View):
    def __init__(self):
        self.template_name = 'course/courses.html'

    def get(self, request):

        return render(request, self.template_name)

class Course(View):
    def __init__(self):
        self.template_name = 'course/course.html'

    def get(self, request):

        return render(request, self.template_name)

class About(View):
    def __init__(self):
        self.template_name = 'course/about.html'

    def get(self, request):

        return render(request, self.template_name)

class Notification(View):
    def __init__(self):
        self.template_name = 'course/notification.html'

    def get(self, request):

        return render(request, self.template_name)

