from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.db import transaction
from django.contrib.auth.models import User

class Authenticate(View):

    def get(self, request):
        return render(request, "login.html")
    
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
                return render(request,"browse.html", {'user': request.user})
            else:
                return render(request, "login.html")
        
