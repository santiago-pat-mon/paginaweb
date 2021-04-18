from django.shortcuts import render, redirect

#Data models
from .models import *

# Django


# Create your views here.

def get_index(request):

    objects={'categories':showCategories(), 'posts':showPosts()}
    return render(request,'index.html',objects)


def showCategories():
    categories = Category.objects.all()
    ctx = { 'categories' : categories }

    return ctx


def showPosts():
    posts = Posts.objects.all()
    ctx = {'posts' : posts}
    
    return ctx


def showBussinesInCategory(request,id):
    business_in_category = Business.objects.filter(category=id)
    ctx = {'business' : business_in_category}

    return render(request,'categoryDetail.html',ctx)


def showBussines(request,id):
    bns = Business.objects.get(id=id)
    ctx = {'bussines' : bns}
    
    return render (request,'bussines.html',ctx)


def showProductsInBussines(id):
    product = Product.objects.filter(business = id)
    ctx={'product' : product}
    return ctx


def showProductsDetails(request,id):
    
    respuesta = Product.objects.get(id = id)
    ctx = {'product' : respuesta}

    return render (request, 'product.html') 

