from django.shortcuts import render

# Create your views here.
from .models import  Contents
from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    return render (request,"home/index.html")