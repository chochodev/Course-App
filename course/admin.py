from django.contrib import admin
from .models import CourseHead, CourseSection, CourseContent

# Register your models here.
admin.site.register(CourseHead)
admin.site.register(CourseSection)
admin.site.register(CourseContent)
