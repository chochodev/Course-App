from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.Courses.as_view(), name='courses'),
    path('course/', views.Course.as_view(), name='course'),
    path('notification/', views.Notification.as_view(), name='notification'),
]