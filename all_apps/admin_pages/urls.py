from django.urls import path
from . import views

urlpatterns = [
    path('panel/', views.AdminPage.as_view(), name='admin'),
    path('create/', views.CreateCourse.as_view(), name='create_course'),
    path('edit/', views.EditCourse.as_view(), name='edit_course'),
]