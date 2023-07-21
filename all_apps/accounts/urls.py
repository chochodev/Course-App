from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('home/', views.Account.as_view(), name='signup'),
    path('accountsettings/', views.AccountSettings.as_view(), name='accountsettings'),
    path('logout/', views.Account.as_view(), name='logout'),

    path('forget_password/',
    auth_views.PasswordResetView.as_view(template_name='accounts/forgetpassword.html'),
    name='forgetpassword'),

    # path('forget_password_done/',
    # auth_views.PasswordResetDoneView.as_view(template_name='accounts/forgetpassword.html'),
    # name='forgetpassworddone')

    path('reset/<uidb64>/<token>/',
    auth_views.PasswordResetConfirmView.as_view(template_name='accounts/forgetpasswordconfirm.html'),
    name='forgetpasswordconfirm'),

    path('forget_password_complete/',
    auth_views.PasswordResetCompleteView.as_view(template_name='accounts/forgetpasswordcomplete.html'),
    name='forgetpasswordcomplete'),

]