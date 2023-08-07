from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views import View
from django.contrib import messages
from django.db import transaction
from django.contrib.auth import authenticate, logout, login

class Authentication(View):

    def get(self, request):
        return render(request, 'login.html')
    
    def post(self, request):
        with transaction.atomic():
            print("POST request recieved")
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(username=username, password=password)

            print("User authentication method is called")

            if user is not None:
                login(request, user)
                obj = User.objects.get(username=username)
                per = obj.get_all_permissions()
                print("Permissions allocated are: ", per, user)
                return redirect("browse")
            else:
                messages.warning(request, "Invalid username or password")
                return redirect("login")
        

