from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import *



class AdminPage(View):
    def __init__(self):
        self.template_name = 'admin.html'

    @method_decorator(login_required(login_url='signup'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):

        return render(request, self.template_name)


class CreateCourse(View):
    def __init__(self):
        self.template_name = 'course/course_create.html'

    @method_decorator(login_required(login_url='signup'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):

        return render(request, self.template_name)


class EditCourse(View):
    def __init__(self):
        self.template_name = 'course/course_edit.html'

    @method_decorator(login_required(login_url='signup'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):

        return render(request, self.template_name)
