from django.shortcuts import render, redirect

#Data models
from .models import *

# Django


# Create your views here.
def showCategories(request):
    categories = Category.objects.all()
    ctx = { 'categories' : categories }

    return render (request, 'index.html', ctx)

