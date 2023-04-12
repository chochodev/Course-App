from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.Account.as_view(), name='signup'),
    path('accountsettings/', views.AccountSettings.as_view(), name='accountsettings'),
    path('logout/', views.Account.as_view(), name='logout'),
]