from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
# Create your views here.
def index(request):
    return render(request, 'index.html')

def booking(request):
    return render(request, 'booking.html')

def profile(request):
    return render(request, 'profile.html')
    
def about(request):
    return render(request, 'about.html')

# Planets
def sun(request):
    return render(request, 'sun.html')

def moon(request):
    return render(request, 'moon.html')

def mercury(request):
    return render(request, 'mercury.html')

def venus(request):
    return render(request, 'venus.html')

def earth(request):
    return render(request, 'earth.html')

def mars(request):
    return render(request, 'mars.html')

def jupiter(request):
    return render(request, 'jupiter.html')

def saturn(request):
    return render(request, 'saturn.html')

def uranus(request):
    return render(request, 'uranus.html')

def neptune(request):
    return render(request, 'neptune.html')

def pluto(request):
    return render(request, 'pluto.html')

# Login

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Authenticate the user
        user = authenticate_custom(username, password)
        
        if user:
            # User authenticated, log them in (or do any other logic)
            # request.session['user_id'] = user.id
            return redirect('index')  # Redirect to home page or desired page
        else:
            # Invalid credentials, show an error message
            messages.error(request, 'Invalid username or password')
    
    return render(request, 'login.html')

def authenticate_custom(username, password):
    try:
        user = Registration.objects.get(username=username)
        if user.password == password:
            return user  # Credentials are valid
        else:
            return None  # Invalid password
    except Registration.DoesNotExist:
        return None  # Username does not exist
# Register
def registration(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = firstname.lower()+lastname.lower()
        if Registration.objects.filter(username=username.lower()).exists():
            messages.error(request, "Username already exists.")
            return redirect('registration')  # Redirect to a page where the user can try again
        else:
            try : 
                obj = Registration(username = username, 
                                phone_number = phone, email_id = email, password = password)
                obj.save()
                messages.success(request, "Username is available.")
                return redirect('login') 
            except:
                messages.error(request, "Username already exists.")
                return redirect('registration') 

    return render(request, 'registration.html')