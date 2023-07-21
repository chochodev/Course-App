from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.CreateCourse.as_view(), name='create'),
    path('edit/', views.EditCourse.as_view(), name='edit'),
]