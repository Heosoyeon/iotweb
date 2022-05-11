from django.shortcuts import render
from django.views import View
from django_request_mapping import request_mapping

@request_mapping("")
class MyView(View):

    @request_mapping("/", method="get")
    def home(self, request):
        return render(request, 'login.html')

    @request_mapping("/forgot-password", method="get")
    def forgot_password(self, request):
        return render(request, 'forgot-password.html')

    @request_mapping("/register", method="get")
    def register(self, request):
        return render(request, 'register.html')