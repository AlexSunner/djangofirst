from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world!")

    if request.method == "POST":
        return HttpResponse("You have POSTed something")
    else:
        return HttpResponse(request.method)