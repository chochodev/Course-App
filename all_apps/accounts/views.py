from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.contrib.messages import constants as custom_messages
from .models import User
from .decorators import authenticated_user


MESSAGE_TAGS = {
    custom_messages: 'signup_error',
    custom_messages: 'signin_error',
}

class Account(View):
    def __init__(self):
        self.template_name = 'accounts/landingpage.html'

    # @unauthenticated_user
    def get(self, request):
        print('get request received')
        return render(request, self.template_name)
        
    @method_decorator(never_cache, name='dispatch')
    @method_decorator(authenticated_user, name='dispatch')
    def post(self, request):
        if 'signup' in request.POST:
            print('post request received')
            # gets the client side data
            username = request.POST.get('username')
            alias = request.POST.get('alias')
            email = request.POST.get('email')
            password = request.POST.get('password')

            # handles existing Email or Alias
            if User.objects.filter(email=email) and User.objects.filter(alias=alias):
                signup_error = 'Alias and Email already exist'
                messages.error(request, signup_error)
                return render(request, self.template_name)
            elif User.objects.filter(email=email):
                signup_error = 'Email already exist'
                messages.error(request, signup_error)
                return render(request, self.template_name)
            elif User.objects.filter(alias=alias):
                signup_error = 'Alias already exist'
                messages.error(request, signup_error)
                return render(request, self.template_name)

            # creates user with the variables gotten from the client side above
            user = User.objects.create_user(username=username, alias=alias, email=email, password=password)

            # login user and redirect to home page
            username = request.user.alias
            login_message = f'Account created and logged in as {username}'
            login(request, user)
            messages.success(request, login_message)
            return redirect('home')

        elif 'signin' in request.POST:
            user = request.user
            if user.is_authenticated:
                login_message = 'You′re already logged in. Please logout to login to another account'
                messages.warning(request, login_message)
                print(login_message)
                return redirect('accountsettings')

            else:
            # gets the client side data
                email = request.POST.get('email')
                password = request.POST.get('password')

                # authenticate
                user = authenticate(request, email=email, password=password)

                # login user and redirect to home page
                if user is not None:
                    login(request, user)
                    username = request.user.username
                    messages.success(request, username)
                    return redirect('home')
                else:
                    try:
                        user = User.objects.get(email=email)
                    except User.DoesNotExist:
                        signin_error = 'Account with this email does not exist'
                        messages.error(request, signin_error)
                        return render(request, self.template_name)

                    if not user.check_password(password):
                        signin_error = 'Incorrect password'
                        messages.error(request, signin_error)
                        return render(request, self.template_name)

                    signin_error = 'Incorrect Email or Password'
                    messages.error(request, signin_error)
                    return render(request, self.template_name)

class AccountSettings(View):
    def __init__(self):
        self.template_name = 'accounts/accountsettings.html'

    @method_decorator(login_required(login_url='signup'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # logging out a user
    def get(self, request):
        user = request.user
        context = {'username':user.username, 'email':user.email, 'alias':user.alias}
        return render(request, self.template_name, context)

    def post(self, request):
        if request.user.is_authenticated and 'logout' in request.POST:
            username = request.user.username
            logout(request)
            logout_message = f'Successfully logged out as {username}'
            context = {'logout_message':logout_message}
            return redirect('/accounts/home', context)
        else: 
            return render(request, self.template_name)
