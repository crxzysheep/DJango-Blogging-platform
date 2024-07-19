from django.shortcuts import render, HttpResponse

# Create your views here.
def welcome_view(request):
    return HttpResponse("ho")