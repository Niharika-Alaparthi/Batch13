from django.shortcuts import render, redirect
from django.contrib.auth.models import User  # For user creation and management
from django.contrib import messages  # For displaying success or error messages
from django.contrib.auth import authenticate, login

def index(request):
    return render(request, 'index.html')  # Render the homepage




def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # Log the user in
            messages.success(request, f'Welcome, {username}!')
            return redirect('/')  # Redirect to home page after login
        else:
            messages.error(request, 'Invalid username or password')
            return render(request, 'app13/signin.html')
    
    return render(request, 'app13/signin.html')  # Render the Sign In page

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        disability = request.POST['disability']
        
        # Check if passwords match
        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return render(request, 'app13/signup.html')
        
        # Check if email is valid
        if not email.endswith('@gmail.com') or '@' not in email:
            messages.error(request, 'Email must be a valid Gmail address (e.g., example@gmail.com)')
            return render(request, 'app13/signup.html')

        # Create the user
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, 'Account created successfully. Please Sign In.')
            return redirect('signin')  # Redirect to the Sign In page
        except Exception as e:
            messages.error(request, f'Error creating account: {str(e)}')
            return render(request, 'app13/signup.html')
    
    return render(request, 'app13/signup.html')  # Render the Sign Up page

