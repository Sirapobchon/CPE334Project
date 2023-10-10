from django.shortcuts import render
from .models import User

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Your login logic here
        # For example, you can check if the username and password match a user in the database
        # and redirect the user to the appropriate page
        
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        # Your registration logic here
        # For example, you can create a new User object and save it to the database
        
    return render(request, 'register.html')