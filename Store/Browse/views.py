from django.shortcuts import render
from django.views import View

class Browse(View):

    def get(self, request):
        return render(request, "browse.html")
    
    def post(self, request):
        user = request.user
        render(request, "browse.html", {'user': user})
