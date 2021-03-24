from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout

from operator import itemgetter



def home(req):
    if req.method == "POST":
        username = req.POST('username')
        password = req.POST('password')

        authUser = authenticate(
            username=username,
            password=password,
        )
        if authUser is not None:
            login(req, authUser)
            return render(req, 'home.html')
        else:
            messages.error(req, 'Invalid Credentials')
        return render(req, 'login.html')
    return render(req, 'home.html')

def loginView(req):
    if req.user.is_authenticated:
        return redirect('/')
    elif req.method == "POST":

        username = req.POST('username')

        password = req.POST('password')

        authUser = authenticate(
            username=username,
            password=password
        )
        if authUser is not None:
            login(req, authUser)
            return redirect('/')
        else:
            messages.error(req, 'Invalid Credentials')
        return render(req, 'login.html')
    return render(req, 'login.html')

def logoutView(req):
    logout(req)
    return redirect('/')


def register(req):
    if req.method == "POST":
        user = User()

        user.fname = req.POST['fname']
        user.lname = req.POST['lname']
        user.email = req.POST['email']
        user.password = req.POST['password']

    return render(req, 'register.html')
