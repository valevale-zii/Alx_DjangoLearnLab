from django.shortcuts import render

from django.shortcuts import render

def home(request):
    return render(request, "blog/home.html")

