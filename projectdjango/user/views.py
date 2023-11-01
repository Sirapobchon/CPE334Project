from django.shortcuts import render
from django.http import JsonResponse
from .models import User

# Create your views here.
class UserList():
    def login(request):
        if request.method == 'POST':
            #csrf_token = request.COOKIES.get('csrftoken')
            username = request.POST.get('username')
            password = request.POST.get('password')
            # Your login logic here
            # For example, you can check if the username and password match a user in the database
            # and redirect the user to the appropriate page
            if username == 'admin' and password == 'admin':
                return JsonResponse({'message': 'Successfully logged in'}, status=200)
            else:
                return JsonResponse({'message': 'Invalid username or password'}, status=400)
            
        return JsonResponse({'message': 'It Broke'}, status=400)
    

    def register(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            
        return JsonResponse({'message': 'Invalid username or password'}, status=400)