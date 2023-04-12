from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from .models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class Account(View):
    def __init__(self):
        self.template_name = 'accounts/landingpage.html'

    def get(self, request):
        print('get request received')
        return render(request, self.template_name)

    def post(self, request):
        if 'signup' in request.POST:
            # gets the client side data
            username = request.POST.get('username')
            alias = request.POST.get('alias')
            email = request.POST.get('email')
            password = request.POST.get('password')

            # creates user with the variables gotten from the client side above
            user = User.objects.create_user(username=username, alias=alias, email=email, password=password)

            # login user and redirect to home page
            login(request, user)
            return redirect('home')

        elif 'signin' in request.POST:
            # gets the client side data
            email = request.POST.get('email')
            password = request.POST.get('password')

            # authenticate
            user = authenticate(request, email=email, password=password)

            # login user and redirect to home page
            if user is not None:
                login(request, user)
                context = {'username' : request.user.username}
                return redirect('home')
            else:
                error_message = 'Incorrect Email or Password'
                context = {'error_message':error_message}
                return render(request, self.template_name, context)

class AccountSettings(View):
    def __init__(self):
        self.template_name = 'accounts/accountsettings.html'

    # logging out a user
    @method_decorator(login_required)
    def get(self, request):
        user = request.user
        context = {'username':user.username, 'email':user.email, 'alias':user.alias}
        return render(request, self.template_name, context)

    def post(self, request):
        if request.user.is_authenticated and 'logout' in request.POST:
            logout(request)
            return redirect('home')
        else: 
            return render(request, self.template_name)

        # logging in a user
        username = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            context = {'error_message': 'Incorrect Email or Password, click forget password to reset your password'}
            return render(request, self.template_name, context)

        