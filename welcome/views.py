from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def home_view(request):
    return render(request, "welcome/welcome.html")

def test_home_view(request):
    return render(request, "welcome/welcome_child.html")
