from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("register"))
    return render(request, "index.html")

def profile(request, query):
    return render(request, "profile.html", {"name": query, "names": ["James", "Jarvis", "David", "Joy"]})

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        new_user = User(username=username, password=password)
        new_user.save()

        login(request, new_user)

        return redirect('/')
    else:
        return render(request, "register.html")

def logout_view(request):
    logout(request)
    redirect("/")