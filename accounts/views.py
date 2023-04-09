from django.shortcuts import render, redirect
from django.views import View


class Account(View):
    def __init__(self):
        self.template_name = 'accounts/landingpage.html'

    def get(self, request):

        return render(request, self.template_name)

    def post(self, request):
        pass

class AccountSettings(View):
    def __init__(self):
        self.template_name = 'accounts/accountsettings.html'

    def get(self, request):

        return render(request, self.template_name)

    def post(self, request):
        pass