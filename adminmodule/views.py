from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
import re


def homepage(request):
    return render(request, 'homepage.html')


def teammateshomepage(request):
    return render(request, 'teammateshomepage.html')


def teamleadhomepage(request):
    return render(request, 'teamleadhomepage.html')


def signup(request):
    return render(request, 'signup.html')


def signup1(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        pass1 = request.POST['password']
        pass2 = request.POST['password1']

        # Check if first_name or last_name contains numbers or special characters
        if not all(map(lambda name: bool(re.search(r'[0-9!@#$%^&*(),.?":{}|<>]', name)) == False,
                       [first_name, last_name])):
            messages.info(request, 'Dont give numbers and special characters as a name')
            return render(request, 'signup.html')

        if len(username) not in [4, 10]:
            messages.info(request,'Username should be length 4 for teamlead registration and length 10 for teammate registration')
            return render(request, 'signup.html')

        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'OOPS! Username already exists')
                return render(request, 'signup.html')
            else:
                user = User.objects.create_user(
                    username=username,
                    password=pass1,
                    first_name=first_name,
                    last_name=last_name,
                    email=email
                )
                user.save()
                messages.info(request, 'Account created successfully')
                return render(request, 'login.html')
        else:
            messages.info(request, 'Password does not match')
            return render(request, 'signup.html')



def login(request):
    return render(request, 'login.html')


def login1(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['password']
        user = auth.authenticate(username=username, password=pass1)
        if user is not None:
            auth.login(request, user)
            if len(username) == 10:
                return redirect('teammateHomePage')
            elif len(username) == 4:
                return redirect('teamleadHomePage')
            else:
                return redirect('homepage')
        else:
            messages.info(request, 'Invalid username or password!')
            return render(request,'login.html')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return render(request,'homepage.html')
