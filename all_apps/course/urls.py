from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.HomePage.as_view(), name='home'),
    path('courses/', views.Courses.as_view(), name='courses'),
    path('course/', views.Course.as_view(), name='course'),
    path('about/', views.About.as_view(), name='about'),
    path('notification/', views.Notification.as_view(), name='notification'),
]